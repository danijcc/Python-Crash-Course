#carpeta 9 video 1,2,3,4,5,6,7,8
#Una clase es una plantilla de la cual vamos a poder crear instancias u objetos
#
#   PERSONA es la clase ------> KARLA es un objeto ------> ARMANDO es un objeto
#clase(plantilla generica)     instancia de la clase      instancia de la clase
#posee atributos y metodos

#se recomienda que el nombre de las clases y el nombre del archivo lleve la notacion
#de mayusculas y minusculas ejm: PersonaAdulta.py, class PersonaAdulta:

class Persona: 
    pass
 
print(type(Persona))

########################################################################
#__init__ metodo inicializador similar al metodo constructor 
#y sirve para agregar caracteristicas o atributos a nuestra 
#clase e inicializarlos un constructor es un metodo para poder crear un objeto
#(self) es un parametro que hace referencia al objeto que se va a crear
#__init__ es un metodo dunder o double underscore
#en vez de self se podria utilizar otro nombre como this y funcionaria igual ojo solo
#como primer parametro
class Persona: 
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre       #atributos nombre, apellido, edad
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona:{self.nombre} {self.apellido} {self.edad }')    

persona1 = Persona('Juan','Perez', 28)#este objeto esta mandando a llamar el metodo constructor
                                      #de nuestra clase
persona1.mostrar_detalle()       

#print(f'Objeto Persona1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()#objeto.metodo
Persona.mostrar_detalle(persona1)#clase.metodo(parametros del objeto) no es lo comun
persona1.telefono = '922370772'#podemos agregar atributos al objeto
print(persona1.telefono)

#print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

#podemos modificar los valores directamente desde el objeto accediendo directamente al
#atributo no es recomendable hacer lo correcto es hacerlo mediante metodos
persona1.nombre = 'Dani Jose'
persona1.apellido = 'Colmenares'
persona1.edad = '34'
print(f'Objeto Persona1: {persona1.nombre} {persona1.apellido} {persona1.edad}')



#clase -> atributo ->metodo
#objeto = instancia de la clase

       


