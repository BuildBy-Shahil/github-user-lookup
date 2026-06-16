from api import API
import tkinter as tk
from tkinter import ttk

class User:
    def __init__(self, manager):
        self.data = API(manager)
        self.manager = manager

        """Tk inter window"""
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("GitHub User Looup")
        self.root.configure(background="#727fa3")

        """Root elements"""
        # Entry Frame
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=5, padx=5)

        # Entry and Label
        self.entry_label = tk.Label(self.entry_frame, text="Name")
        self.entry = tk.Entry(self.entry_frame, width=50)
        self.entry_label.grid(row=0, column=0, padx=2.5)
        self.entry.grid(row=0, column=1, padx=2.5)

        """Button"""
        # Button frame
        self.btn_frame = tk.Frame(self.root, background="#4d5875")
        self.btn_frame.pack(padx=5, pady=5)

        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure(
            "Custom.TButton",
            bordercolor="black",
            lightcolor="black",
            darkcolor="black",
            padding=(10, 100, 10, 100),
            font=("Minecraft", 15, "bold"),
            foreground="grey",
            background="#bababa",
        )

        self.submit_btn = ttk.Button(self.btn_frame, text="Submit", style="Custom.TButton", command=self.get_input)
        self.submit_btn.grid(row=0, column=0, pady=5, padx=5)

        self.export_btn = ttk.Button(self.btn_frame, text="Extract", style="Custom.TButton", command=self.manager.fetch)
        self.export_btn.grid(row=0, column=1, padx=5, pady=5)


    def get_input(self):
        name = self.entry.get()
        if name:
            self.data.get_api_data(name)