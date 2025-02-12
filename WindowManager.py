'''
Archivo: WindowManager
DESCRIPCION: Clase que se encarga de gestionar la vista de la aplicación.
Mostrando la información de la tabla de datos del ICBF.
'''

import tkinter as tk
from BusinessLogic.DocManager import DocManager  # Importar la clase DocManager
from Views.DocEditionModal import show_doc_edition  # Importar la función para mostrar modal
from tkinter import messagebox


# Crear una instancia de DocManager y obtener los datos
doc_manager = DocManager()

# Crea una instancia de la ventana principal de la aplicación
root = tk.Tk()

# Define el ancho y el alto, respectivamente, de la ventana
# principal de la aplicación
root.geometry("1024x576")

# Define el título de la ventana principal de la aplicación
root.title("Gesto de Datos del ICBF")

# Crear Frame para contener los Labels
frame = tk.Frame(root, bg="lightgray")
frame.pack(fill=tk.X)  # Expandir en el eje X

'''
============================================= [LABELS] =======================================================
Crear Labels con margen interno para cumplir con
el formato especificado por el docente
'''
label1 = tk.Label(frame, text="Menú Principal", bg="lightgray", font=("Arial", 12))
label1.pack(fill=tk.X, pady=(15,0))

label2 = tk.Label(frame, text="Equipo: E1   |   Nombre: Andrés Felipe Muñoz Aguilar (2210087)", bg="lightgray", font=("Arial", 12))
label2.pack(fill=tk.X, pady=(15,0))

#Colocar un padding final al frame
bottomPadding = tk.Label(frame, bg="lightgray")
bottomPadding.pack(fill=tk.X, pady=(0,0))
#=======================================================================================================



'''
============================================= [BOTONES] =======================================================
Crear los botones que permitirán llamar a la clase
que administrará los datos que se carguen del csv
y una tabla para mostrar datos
'''

# Crear un frame principal para contener los botones y la tabla
main_frame = tk.Frame(root, bg="lightgray")
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Crear un frame para contener los botones a la izquierda
button_frame = tk.Frame(main_frame, bg="lightgray")
button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

# Crear botón para la opción A con anchura especificada
optionABttn = tk.Button(button_frame, text="a. Mostrar Datos.", font=("Arial", 14), width=20, anchor='w')
optionABttn.pack(pady=(10, 0), padx=(15, 0), anchor='w')

# Crear botón para la opción B con anchura especificada
optionBBttn = tk.Button(button_frame, text="b. Informe Especial.", font=("Arial", 14), width=20, anchor='w')
optionBBttn.pack(pady=(20, 0), padx=(15, 0), anchor='w')

# Crear botón para la opción C con anchura especificada
optionCBttn = tk.Button(button_frame, text="c. Operaciones", font=("Arial", 14), width=20, anchor='w')
optionCBttn.pack(pady=(20, 0), padx=(15, 0), anchor='w')

# Crear botón para la opción D con anchura especificada y alinear el texto a la izquierda
optionDBttn = tk.Button(button_frame, text="d. Salir", font=("Arial", 14), width=20, anchor='w')
optionDBttn.pack(pady=(20, 0), padx=(15, 0), anchor='w')


#=======================================================================================================

'''
============================================= [TABLA] =======================================================
Crear una tabla para mostrar los datos del ICBF
'''

# Crear un frame para contener la tabla a la derecha
table_frame = tk.Frame(main_frame, bg="white")
table_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# ============= [FUNCIONES DE LOS BOTONES] =============
def aButtonEvent():

    '''
    Función que se ejecuta al presionar el botón optionABttn.
    Se encarga de obtener los datos del ICBF y mostrarlos en una tabla.
    '''

    # Limpiar la tabla antes de mostrar los nuevos datos
    for widget in table_frame.winfo_children():
        widget.destroy()

    data = doc_manager.get_data_in_format("lista")

    # Crear la tabla con los datos obtenidos
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            cell = tk.Label(table_frame, text=value, borderwidth=0, relief="solid", font=("Arial", 12))
            cell.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

    # Configurar el grid para que las columnas y filas se expandan
    for i in range(len(data[0])):
        table_frame.grid_columnconfigure(i, weight=1)
    for i in range(len(data)):
        table_frame.grid_rowconfigure(i, weight=1)


def bButtonEvent():
    '''
    La presente función sirve para obtener el informe especial
    del cual se habla en el punto "b" del trabajo.
    Esta función ejecuta la función "get_special_inform" de la clase
    DocManager y muestra el resultado en la tabla. La función 
    "get_special_inform" retorna una lista de listas con los datos
    de menores agrupados por ciudad y sexo, asi como los datos 
    agrupados por ciudad y edad.
    
    Parameters: None

    Returns: None
    '''

    data = doc_manager.get_special_inform()

    # Limpiar la tabla antes de mostrar los nuevos datos
    for widget in table_frame.winfo_children():
        widget.destroy()

    # Mostrar la primera tabla
    for i, row in enumerate(data[0]):
        for j, value in enumerate(row):
            cell = tk.Label(table_frame, text=value, borderwidth=0, relief="solid", font=("Arial", 12))
            cell.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

    # Espacio horizontal entre las tablas
    separator = tk.Label(table_frame, text="", borderwidth=0, relief="solid", font=("Arial", 12))
    separator.grid(row=len(data[0]), column=0, columnspan=len(data[0][0]), pady=10)

    # Mostrar la segunda tabla
    for i, row in enumerate(data[1]):
        for j, value in enumerate(row):
            cell = tk.Label(table_frame, text=value, borderwidth=0, relief="solid", font=("Arial", 12))
            cell.grid(row=i + len(data[0]) + 1, column=j, padx=1, pady=1, sticky="nsew")

    # Configurar el grid para que las columnas y filas se expandan
    for i in range(len(data[0][0])):
        table_frame.grid_columnconfigure(i, weight=1)
    for i in range(len(data[0]) + len(data[1]) + 1):
        table_frame.grid_rowconfigure(i, weight=1)


def cButtonEvent():
    '''
    Función que se ejecuta al presionar el botón optionCBttn.
    Se encarga de mostrar la ventana modal para realizar operaciones
    con los datos del ICBF.
    '''

    show_doc_edition()


def dButtonEvent():
    '''
    Función que se ejecuta al presionar el botón optionDBttn.
    Se encarga de cerrar la aplicación.
    '''

    if messagebox.askyesno("Salir", "Si sale ahora, sus datos serán gaurdados. ¿Desea guardar los datos y salir?"):
        doc_manager.save_df_to_csv()
        root.destroy()

    

# Asignar la función aButtonEvent al botón optionABttn
optionABttn.config(command=aButtonEvent)

optionBBttn.config(command=bButtonEvent)

optionCBttn.config(command=cButtonEvent)

optionDBttn.config(command=dButtonEvent)
#=======================================================================================================


# Inicia el bucle principal de la aplicación para que la ventana se mantenga abierta
root.mainloop()
