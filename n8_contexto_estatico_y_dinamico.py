# carpeta 14 video 3,4,5
#contexto estatico y dinamico
class MiClase:

    variable_clase = 'valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    
   
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
    #con un metodo instancia podemos acceder a los metodos de clase y estatico
    def metodo_de_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

MiClase.metodo_clase()
miObjeto1 = MiClase('variable_instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_de_instancia()

# ----------CONTEXTO ESTATICO--------
#
# from (MODULO - ARCHIVO) import CLASE 
# 
# class MiClase:
#   varible_de_clase = 'valor variable clase'
#   def metodo_de_clase_o_estatico(PARAMETRO-recibe):
#       ATRIBUTOS ->  puede ser de clase estaticos o de clase
#
#
# ---------CONTEXTO DINAMICO--------
#
# OBJETO = <NOMBRE_DE_LA_CLASE>(ARGUMENTO-envia) 
#
#--------------------------------------------------------------------------
# EL CONTEXTO DINAMICO SI PUEDE ACCEDER AL CONTEXTO ESTATICO PERO
# UNA CLASE NO PUEDE ACCEDER A UNA VARIBLE DE INSTANCIA 
#---------------------------------------------------------------------------
#Parametros = son las variables de la funcion 
#Argumentos = es la informacion que vamos a enviar o asignar a la variable
#             o parametro de mi funcion 