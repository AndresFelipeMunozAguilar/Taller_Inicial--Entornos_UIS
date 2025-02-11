'''
Archivo: WindowManager
DESCRIPCION: Clase que se encarga de gestionar la vista de la aplicación.
Mostrando la información de la tabla de datos del ICBF.
'''

import tkinter as tk
from BusinessLogic.DocManager import DocManager  # Importar la clase DocManager

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
optionABttn = tk.Button(button_frame, text="a. Cargar Datos.", font=("Arial", 14), width=20, anchor='w')
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

# Crear una instancia de DocManager y obtener los datos
doc_manager = DocManager()
data = doc_manager.get_data_in_format("lista")

# Crear la tabla con los datos obtenidos
for i, row in enumerate(data):
    for j, value in enumerate(row):
        cell = tk.Label(table_frame, text=value, borderwidth=1, relief="solid", font=("Arial", 12))
        cell.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

# Configurar el grid para que las columnas y filas se expandan
for i in range(len(data[0])):
    table_frame.grid_columnconfigure(i, weight=1)
for i in range(len(data)):
    table_frame.grid_rowconfigure(i, weight=1)
#=======================================================================================================


# Inicia el bucle principal de la aplicación para que la ventana se mantenga abierta
root.mainloop()
