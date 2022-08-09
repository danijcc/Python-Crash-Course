#carpeta 10 video 1
#se le llama encapculamiento cuando solo podemos acceder o modificar los atributos
# desde la misma clase no desde el objeto 

#_nombre  se utiliza guion bajo  bajo para poner restriccion de acceder a esos 
#atributos solo como sugerencia
# __nombre se utiliza doble guion bajo para poner restriccion de acceder a esos  
# atributos denegando la modificacion del mismo  
#a estos atributos con guion bajo los llamamos atributos encapsulados

class Persona: 
    def __init__(self, nombre, apellido, edad,):
        self.__nombre = nombre 
        self.apellido = apellido
        self.edad = edad
       

    def mostrar_detalle(self):
        print(f'Persona:{self.__nombre} {self.apellido} {self.edad }')    

persona1 = Persona('Juan','Perez', 28, )
persona1.__nombre = 'Pedro Diaz'   
persona1.mostrar_detalle()  








