#metodos estaticos y metodo de clase
# carpeta 14 video 4
#------------------los metodos estaticos------------------------ 
# se asocian a la clase en si misma tambien igual que una 
# variable de clase
class MiClase:

    variable_clase = 'valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    
    #para llamar a un metodo estatico la llamamos con el decorador
    #un metodo estatico no puede acceder a la variable self ni a varibles
    #de instacias pero si a la variable de clase variable_clase
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
        #no podemos acceder directamente a la variable de clase si no accedmos
        #a la clase primero y luego a la variable de clase
        #print(variable_clase)

    #metodo de clase tiene relacion con la clase con las variables 
    #cls podemos acceder a las variables de clase de manera directa
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)


MiClase.metodo_clase()