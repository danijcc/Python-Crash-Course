# carpeta 14 video 1,2
# una variable de clase es una clase la cual las variables se asocian 
# directamente con la clase y no con los objetos 
# cualquier objeta que acceda a una variable de clase va a ver la misma 
# informacion no tendran valores distintos entre cada objeto si no que van
# acceder directamente a la variable de clase que se a definido
# para definir una variable de clase la definimos fuera de cualquier
# metodo de la clase

class MiClase:
    variable_clase ='valor variable clase'
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

#para acceder a  una variable de clase no es necesario crear un objeto
#lo podemos hacer direcctamente
print(MiClase.variable_clase)

#para acceder a la variable de insancia si debemos crear un objeto
miClase = MiClase('valor variable instancia')
print(miClase.variable_instancia)
#tambien podemos recuparar el valor de la variable de clase 
print(miClase.variable_clase)
#variable de clase en cualquier momento en python todas las clases a la 
#vez son objetos
MiClase.variable_clase2 = 'Valor variable clase 2'
#distinto valor en la variable de instancia
miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
#podemos acceder a la variable desde el objeto 1 o 2 creado o desde la clase 
print(MiClase.variable_clase2)
print(miClase.variable_clase2)
print(miClase2.variable_clase2)
