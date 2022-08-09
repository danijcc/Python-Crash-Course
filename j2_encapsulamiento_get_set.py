 #carpeta 10 video 2,3
 #__nombre restringe acceso para que no se pueda modificar directamente los atributos 
 #solo los podremos acceder por los metodos get y set
 #get = obtener/recuperar :los atributos de nuestra clase
 #set = colocar/modificar :los atributos de nuestra clase
 #@property = con el decorador @property indicamos que va a acceder al atributo 
 #en el metodo indicado solo pudiendo acceder con este metodo y encapsulando el 
 #atributos indicado si solo dejamos el decorador get se dice que es una variable 
 #de solo lectura
 #@nombre.setter = decorador de tipo set con el nombre del atributo seguido de la
 # palabra setter permitira modificar el atributo indicado en este caso _nombre 
class Persona: 
    def __init__(self, nombre, apellido, edad,):
        self._nombre = nombre 
        self._apellido = apellido
        self._edad = edad

    @property 
    def nombre(self): #este es un metodo get
        print('llamando metodo get nombre')
        return self._nombre
       
    @nombre.setter
    def nombre(self, nombre):
        print('llamando metodo set nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    
    def mostrar_detalle(self):
        print(f'Persona:{self._nombre} {self._apellido} {self._edad }')    

persona1 = Persona('Juan','Perez', 28, )
persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Lara'
persona1.edad = 30
persona1.mostrar_detalle()
#print(persona1.nombre)








