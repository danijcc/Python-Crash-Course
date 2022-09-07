#metodos estaticos y metodo de clase
# carpeta 14 video 3,4
#------------------los metodos estaticos------------------------ 
# se asocian a la clase en si misma tambien igual que una 
# variable de clase


class MiClase:

    variable_clase = 'valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    
    #para llamar a un metodo estatico la llamamos con el decorador @staticmethod
    #un metodo estatico no puede acceder a la variable self ni a varibles
    #de instacias pero si a la variable de clase variable_clase
    #Un metodo estatico no tiene relacion directa con nuestra clase
    #no resibe ninguna inf de la clase en si misma
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
        #no podemos acceder directamente a la variable de clase si no accedmos
        #a la clase primero y luego a la variable de clase
        #print(variable_clase)

    #para definir un metodo de clase vamos a usar el siguiente decorador
    #por convension es cls que significa clases 
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

MiClase.metodo_clase()
#MiClase.metodo_estatico()