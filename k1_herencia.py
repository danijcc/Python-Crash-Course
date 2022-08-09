#carpeta 11 video 1,2
#clase padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
    
    def __str__(self):
        return f'Persona: [Nombre: {self.nombre} Edad: {self.edad}]'
        

#clase hija o sub clase
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)#llama el metodo inicializador de la clase padre
        self.sueldo = sueldo 

    def __str__(self):
        return f'Empleado: [Sueldo: {self.sueldo}] {super().__str__()}'
 

empleado1 = Empleado('Juan', 28, 50000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)