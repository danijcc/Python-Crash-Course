# carpeta 14 video 7
# 1 declaramos nuestra variable de clase y la inicializamos
# 2 definimos un metodo inicializador tambien conocido como main o constructor
# 3 mediante la clase accedemos a la variable de clase y la incrementamos
# 4 asignamos el valor al atributo id_persona atravez de Persona.contador_personas
class Persona:
    contador_personas = 0 #1
    
    def __init__(self, nombre, edad): #2
        Persona.contador_personas += 1 #3
        self.id_persona = Persona.contador_personas #4
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'


#creamos un objeto
# con if __name__=='__main__': validamos que solo se ejecute el siguiente codigo en 
#este archivo solamente
if __name__=='__main__':
    persona1 = Persona('Juan', 28)
    print(persona1)
    persona2 = Persona('Juan', 28)
    print(persona2)
    persona3 = Persona('Juan', 28)
    print(persona3)
#la siguiente propiedad permite saber el nombre del modulo que se esta ejecutando
#bien sea main = principal u algo otro declarado
print(__name__)

