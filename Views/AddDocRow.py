import tkinter as tk
from tkinter import ttk

class AddDocRow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.crear_contenido()

    def crear_contenido(self):
        etiqueta = tk.Label(self, text="Contenido de la Pestaña 2", font=("Arial", 12))
        etiqueta.pack(pady=20)
