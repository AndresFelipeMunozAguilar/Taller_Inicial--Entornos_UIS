import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter import Toplevel
from Views.DelDocRow import DelDocRow
from Views.AddDocRow import AddDocRow
from Views.EditDocRow import EditDocRow


def show_doc_edition():
    """Función para crear una ventana modal en Tkinter."""
    modal = Toplevel()  # Crear la ventana modal
    modal.title("Editar documento")  # Título de la ventana
    modal.geometry("360x640")  # Tamaño de la ventana

    # Hacer que la ventana sea modal (bloquea la principal)
    modal.transient()  # Indica que esta ventana pertenece a otra
    modal.grab_set()   # Evita que el usuario interactúe con la ventana principal hasta cerrar esta

       # Crear el contenedor de pestañas (Notebook)
    notebook = ttk.Notebook(modal)
    notebook.pack(expand=True, fill="both")

    # Crear e insertar las pestañas usando clases importadas
    pestaña1 = DelDocRow(notebook)
    pestaña2 = AddDocRow(notebook)
    pestaña3 = EditDocRow(notebook)


    notebook.add(pestaña1, text="Delete Row")
    notebook.add(pestaña2, text="Add Row")
    notebook.add(pestaña3, text="Edit Row")


    # Botón para cerrar la ventana modal
    boton_cerrar = tk.Button(modal, text="Cerrar", font=('Arial', 12), padx=5, pady=5, command=modal.destroy)
    boton_cerrar.pack(pady=15)

    # Mantener la ventana modal abierta
    modal.mainloop()
