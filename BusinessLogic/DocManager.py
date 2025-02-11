import pandas as pd
import numpy as np
import os

class DocManager:
    _instance = None  # Variable de clase para almacenar la única instancia

    @property
    def csv_path(self):
        return self._csv_path

    @property
    def df(self):
        return self._df
    
    @property
    def mapeo_ciudades(self):
        return {
            1: 'Bucaramanga',
            2: 'Girón',
            3: 'Florida',
            4: 'Piedecuesta'
        }

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DocManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):  # Verificar si ya ha sido inicializado
            self._csv_path = os.path.join(os.path.dirname(__file__), "../DataBase/chicos.csv")
            self._df = pd.read_csv(self._csv_path, header=None)  # Leer CSV sin nombres de columnas

            self._df.columns = ['Codigo', 'Sexo', 'Nombre', 'Edad', 'Ciudad'] 
            self._initialized = True  # Marcar como inicializado

    def get_data_in_format(self, format):

        '''
        Esta función toma los datos del dataframe almacenado en esta clase
        y los devuelve en el formato especificado por el parámetro format.

        Parámetros:
        format -- El formato en el que se desea obtener los datos. Puede ser
        (string) 'lista'.

        Retorna:
        Los datos en el formato especificado por el parámetro format.
        En caso de seleccionar un formato no soportado, se retorna None.
        '''

        datos = None

        if( format == 'lista'):

            df_copy = self._df.copy()  # Copiar el dataframe para no modificar el original
            
            df_copy['Sexo'] = df_copy['Sexo'].map({
                'F': 'Femenino',
                'M': 'Masculino'
            })

            df_copy['Ciudad'] =df_copy['Ciudad'].map( 
                self.mapeo_ciudades
            )

            datos = df_copy.values.tolist() # Convertir a lista de listas

            columnas = df_copy.columns.tolist()  # Nombres de las columnas
            datos = [columnas] + datos  # Datos para tkinter (lista de listas)

        return datos    


    # Definir los rangos de edad
    def asignar_grupo_etario(self, edad):
        if edad <= 5:
            return "0 - 5 años"
        elif edad <= 10:
            return "6 - 10 años"
        else:
            return "Mayor de 10 años"


    def get_special_inform(self):

        '''
        La presente función sirve para obtener el informe especial
        del cual se habla en el punto "b" del trabajo. 
        Esta función cambia el formato de los datos en la columna de ciudad
        de entero a un string con la ciudad correspondiente. El género lo pasa
        de (F ó M) a (Femenino ó Masculino).
        Además, muestra los totales por ciudad y su porcentaje de participación
        respecto al gran total. 
        Finalmente, se muestra el número de menores de edad en cada grupo etáreo.
        Los grupos son los siguientes:

        1. 0 - 5 años
        2. 6 - 10 años
        3. Mayor de 10 años

        Retorna:
        Una lista de listas con los datos del informe especial.
        '''


        total_children = len(self._df)  # Total de niños

        #====================================== [Creacion tabla 1] ===========================================
        # Agrupar a los menores por ciudad y contar cuantos hay de 
        # cada sexo
        df_copy = self._df.copy()  # Copiar el dataframe para no modificar el original  
        city_count = df_copy.groupby(['Ciudad', 'Sexo']).size().unstack(fill_value=0)

        # Renombrar las columnas
        city_count.columns =  ["Total Hembras", "Total Varones"]

        # Calcular los ratios dividiendo por el total de personas
        city_count["Ratio Hembras"] = city_count["Total Hembras"].astype(str) + "/" + str(total_children)
        city_count["Ratio Varones"] = city_count["Total Varones"].astype(str) + "/" + str(total_children)

        # Restablecer el índice para que "ciudad" sea una columna normal
        city_count = city_count.reset_index()

        
        # Cambiar los códigos de ciudad por los nombres de las ciudades
        city_count['Ciudad'] = city_count['Ciudad'].map({
            1: 'Bucaramanga',
            2: 'Girón',
            3: 'Florida',
            4: 'Piedecuesta'
        }) 



        datos_tabla_1 = city_count.values.tolist()  # Convertir a lista de listas
        columnas_tabla_1 = city_count.columns.tolist()
        tabla_1 = [columnas_tabla_1] + datos_tabla_1  # Datos para tkinter (lista de listas)


        #=======================================================================================================

        
        #====================================== [Creacion tabla 2] ===========================================
        
        '''
        Ahora, se va a crear una tabla, agrupando a los menores por grupos etareos.
        Los grupos etareos son los siguientes:

        1. 0 - 5 años
        2. 6 - 10 años
        3. Mayor de 10 años
        '''

                
        # Agregar columna de grupo etario sin modificar el DataFrame original
        df_copy["Grupo Etario"] = df_copy["Edad"].apply(self.asignar_grupo_etario)

        # Contar la cantidad de menores por ciudad y grupo etario
        age_count = df_copy.groupby(["Ciudad", "Grupo Etario"]).size().unstack(fill_value=0)

        age_count = age_count.reset_index()  # Restablecer el índice para que "ciudad" sea una columna normal

        # Renombrar las columnas
        age_count.columns = [
            "Ciudad",
            "Menores de 5 años", 
            "Entre 6 y 10 años", 
            "Mayores de 10 años"
        ]   

        # Cambiar los códigos de ciudad por los nombres de las ciudades
        age_count['Ciudad'] = age_count['Ciudad'].map({
            1: 'Bucaramanga',
            2: 'Girón',
            3: 'Florida',
            4: 'Piedecuesta'
        }) 
        
        datos_tabla_2 = age_count.values.tolist()  # Convertir a lista de listas
        columnas_tabla_2 = age_count.columns.tolist()
        tabla_2 = [columnas_tabla_2] + datos_tabla_2  # Datos para tkinter (lista de listas)

        return [tabla_1, tabla_2]
    

    def delete_row( self, codigo ):
        index_to_delete = self._df[self._df['Codigo'] == codigo].index
        if not index_to_delete.empty:
            self._df = self._df.drop(index_to_delete)
            return True
        return False

