#carpeta 10 video 5,6
#si queremos importar todas las clases del modulo utilizariamos un *
#from j3_Persona import *
from j3_Persona import Persona 

# con if __name__=='__main__': validamos que solo se ejecute el siguiente codigo en 
#este archivo solamente y no traiga datos de la clase o modulo principal
if __name__=='__main__':
    persona1 = Persona('Karla','Gomez', 30)
    persona1.mostrar_detalle()


#la siguiente propiedad permite saber el nombre del modulo que se esta ejecutando
#bien sea main = principal u algo otro declarado
    print(__name__)