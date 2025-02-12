import tkinter as tk
from tkinter import ttk
from BusinessLogic.DocManager import DocManager
from tkinter import messagebox

class EditDocRow(ttk.Frame):


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

    @property
    def doc_manager(self):
        return self._doc_manager

    def __init__(self, parent):
        super().__init__(parent)
        self.crear_contenido()
        self._doc_manager = DocManager()

    def edit_row(self):

        try:
            codigo = int(self.entry_codigo.get())
        except ValueError:
            messagebox.showerror("Error", "El código debe ser un número entero.")
            return


        campo = self.combobox_campo.get()
        valor = self.entry_valor.get()
        
        if( campo == "Codigo" or campo == "Edad" or campo == "Ciudad" ):

            try:
                valor = int(valor)
            except ValueError:
                messagebox.showerror("Error", "El valor debe ser un número entero.")
                return
            
        
        elif( campo == "Sexo" or campo == "Nombre" ):
            valor = str(valor)
        else:
            messagebox.showerror("Error", "Campo no encontrado.")
            

        try:
            error_text = None

            if ((campo == 'Ciudad') and (valor not in self.mapeo_ciudades)):
                error_text = f"Ciudad no encontrada. La ciudad debe ser un número entre {min(self.mapeo_ciudades.keys())} y {max(self.mapeo_ciudades.keys())}"
            elif ((campo == 'Sexo') and (valor not in self.mapeo_sexos)):
                sexos = ", ".join(self.mapeo_sexos.keys())
                error_text = f"Sexo no encontrado. El sexo debe tener alguno de estos valores: {sexos}."


            if error_text:
                raise ValueError(error_text)
                        
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return



        if( self.doc_manager.edit_row(codigo, campo, valor) ):
            messagebox.showinfo("Éxito", "La edición fue exitosa.")
        else:
            messagebox.showerror("Error", "Código no encontrado.")




    def crear_contenido(self):
        etiqueta = tk.Label(self, text="Esta ventana permite editar una fila de la tabla. Por favor, escriba el código de la fila que quiere editar y escoja el campo que quiere cambiar.", font=("Arial", 12), wraplength=350)
        etiqueta.pack(pady=10, fill='x', padx=10)

        # Añadir los nuevos elementos
        label_codigo = tk.Label(self, text="Encontrar el código:", font=("Arial", 10))
        label_codigo.pack(anchor='w', padx=10)
        
        self.entry_codigo = tk.Entry(self)
        self.entry_codigo.pack(fill='x', anchor='w', padx=10, pady=(0, 10))

        label_campo = tk.Label(self, text="Editar el campo:", font=("Arial", 10))
        label_campo.pack(anchor='w', padx=10)
        
        campo_opciones = ["Codigo", "Sexo", "Nombre", "Edad", "Ciudad"]
        self.combobox_campo = ttk.Combobox(self, values=campo_opciones, state="readonly")
        self.combobox_campo.pack(fill='x', anchor='w', padx=10, pady=(0, 10))

        label_valor = tk.Label(self, text="Reemplazar con el siguiente valor:", font=("Arial", 10))
        label_valor.pack(anchor='w', padx=10)
        
        self.entry_valor = tk.Entry(self)
        self.entry_valor.pack(fill='x', anchor='w', padx=10, pady=(0, 10))

        # Añadir el botón
        boton = tk.Button(self, text="Imprimir Valores", command=self.edit_row)
        boton.pack(pady=10)



