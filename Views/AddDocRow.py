import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from BusinessLogic.DocManager import DocManager

class AddDocRow(ttk.Frame):

    @property
    def doc_manager(self):
        return self._doc_manager


    @property
    def mapeo_ciudades(self):
        return {
            1: 'Bucaramanga',
            2: 'Girón',
            3: 'Florida',
            4: 'Piedecuesta'
        }
    
    @property
    def mapeo_sexos(self):
        return{
            'F': 'Femenino',
            'M': 'Masculino'
        }

    def __init__(self, parent):
        
        self._doc_manager = DocManager()
        
        super().__init__(parent)
        
        self.crear_contenido()



    def añadir_fila(self):
        try:
            codigo = int(self.codigo_entry.get())
            sexo = str(self.sexo_combobox.get())
            nombre = str(self.nombre_entry.get())
            edad = int(self.edad_entry.get())
            ciudad = int(self.ciudad_combobox.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos en todos los campos.")
            return
        
        if self.doc_manager.add_row(codigo, sexo, nombre, edad, ciudad):
            messagebox.showinfo("Éxito", "La fila fue añadida con éxito.")
        else:
            messagebox.showerror("Error", "El código ya existe.")


    def crear_contenido(self):
        etiqueta = tk.Label(self, text="Esta ventana permite añadir una fila de la tabla, para ello, se requiere que especifique los siguientes campos.", font=("Arial", 12), wraplength=350)
        etiqueta.pack(pady=10, fill='x', padx=10)

        # Código: Input text box
        tk.Label(self, text="Código:").pack(anchor='w')
        self.codigo_entry = tk.Entry(self)
        self.codigo_entry.pack(fill='x', pady=5, padx=10)

        sexo_texto = 'Los sexos disponibles son:\n'
        sexo_texto = sexo_texto + ("\n".join([f"{key}. {value}" for key, value in self.mapeo_sexos.items()]))
        etiqueta2 = tk.Label(self, text=sexo_texto, font=("Arial", 10), wraplength=350, anchor='w', justify='left')
        etiqueta2.pack(pady=10, fill='x', padx=10)


        # Sexo: combobox
        tk.Label(self, text="Sexo:").pack(anchor='w')
        self.sexo_combobox = ttk.Combobox(self, values=["F", "M"], state="readonly")
        self.sexo_combobox.pack(fill='x', pady=5, padx=10)

        # Nombre: Input text box
        tk.Label(self, text="Nombre:").pack(anchor='w')
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(fill='x', pady=5, padx=10)

        # Edad: Input text box
        tk.Label(self, text="Edad:").pack(anchor='w')
        self.edad_entry = tk.Entry(self)
        self.edad_entry.pack(fill='x', pady=5, padx=10)

  
        ciudades_texto = 'Las ciudades disponibles son:\n'
        ciudades_texto = ciudades_texto + ("\n".join([f"{key}. {value}" for key, value in self.mapeo_ciudades.items()]))
        etiqueta2 = tk.Label(self, text=ciudades_texto, font=("Arial", 10), wraplength=350, anchor='w', justify='left')
        etiqueta2.pack(pady=10, fill='x', padx=10)

        # Ciudad: Combobox
        tk.Label(self, text="Ciudad:").pack(anchor='w')
        self.ciudad_combobox = ttk.Combobox(self, values=[1, 2, 3, 4], state="readonly")
        self.ciudad_combobox.pack(fill='x', pady=5, padx=10)

        # Botón para añadir fila
        self.add_button = tk.Button(self, text="Añadir fila", command=self.añadir_fila)
        self.add_button.pack(pady=10)
