import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from BusinessLogic.DocManager import DocManager

class DelDocRow(ttk.Frame):

    @property
    def doc_manager(self):
        return self._doc_manager

    def __init__(self, parent):
        super().__init__(parent)
        self._doc_manager = DocManager()
        self.crear_contenido()

    def delete_row(self):
        codigo = self.codigo_entry.get()
        try:
            codigo = int(codigo)
            self.doc_manager.delete_row(codigo)
        except ValueError:
            messagebox.showwarning("Advertencia", "El código debe ser un número.")

    def crear_contenido(self):
        etiqueta = tk.Label(self, text="Esta ventana permite eliminar una fila de la tabla, usando como parámetro el código del menor de edad.", font=("Arial", 12), wraplength=350)
        etiqueta.pack(pady=10, fill='x')

        formulario_frame = ttk.Frame(self)
        formulario_frame.pack(pady=10)

        codigo_label = tk.Label(formulario_frame, text="Código:", font=("Arial", 10))
        codigo_label.grid(row=0, column=0, padx=5, pady=5)

        self.codigo_entry = tk.Entry(formulario_frame, font=("Arial", 10))
        self.codigo_entry.grid(row=0, column=1, padx=5, pady=5)

        eliminar_button = tk.Button(self, text="Eliminar")
        eliminar_button.pack(pady=10)

        eliminar_button.config(command=self.delete_row)


