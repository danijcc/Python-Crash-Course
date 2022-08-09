#carpeta 9 video 15
class Persona: 
    def __init__(self, nombre, apellido, edad, *tupla, **diccionario):#pasar tupla y diccionario
        self.nombre = nombre       
        self.apellido = apellido
        self.edad = edad
        self.tupla = tupla
        self.diccionario = diccionario

    def mostrar_detalle(self):
        print(f'Persona:{self.nombre} {self.apellido} {self.edad } {self.tupla} {self.diccionario}')    

persona1 = Persona('Juan','Perez', 28, '87658765878', 2, 3, 5, m='manzana', p='pera')
persona1.mostrar_detalle()       

persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()






