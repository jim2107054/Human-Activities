import cv2
import numpy as np
from ultralytics import YOLO
import tkinter as tk
from tkinter import messagebox, Scrollbar
from PIL import Image, ImageTk
import threading

model = YOLO("yolov8n.pt")
names = model.model.names

class BlurApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Track Id Blur Tool with Dual View")
        self.root.geometry("1150x780")
        self.root.resizable(False,False)

        self.capture = None
        self.video_writer = None
        self.running = False
        self.paused = False
        self.frame = None
        self.annotated_frame = None
        self.original_frame = None
        self.blur_mode = False

        self.out_w, self.out_h = 480, 360
        self.fps = 30

        self.selected_ids = set()
        self.track_ids_ui = set()
        self.checkbuttons = {}
        self.check_vars = {}

        self.setup_ui()

    def setup_ui(self):
        # Frame for Both video views
        video_frame = tk.Frame(self.root)
        video_frame.pack(pady=5)

        self.video_label_original = tk.Label(video_frame, text="Original Frame")
        self.video_label_original.pack(side="left",padx=5)

        # Track Id checkboxes
        track_id_frame = tk.Frame(self.root)
        track_id_frame.pack(padx=10, fill="x")

        canvas = tk.Canvas(track_id_frame, height=60)
        h_scroll = Scrollbar(track_id_frame, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=h_scroll.set)



