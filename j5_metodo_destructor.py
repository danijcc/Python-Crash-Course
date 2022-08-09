 #carpeta 10 video 7
#el metodo destructor se manda a llamar para liberar recursos
#cuando eliminamos un objeto el meto destructor se manda allamar de manera automatica
#def __del__(self):

from j3_Persona import Persona 

print('Creacion de Objetos'.center(30,'-'))
persona1 = Persona('Karla','Gomez', 30)
persona1.mostrar_detalle()

print('Eliminacion de objetos'.center(30,'-'))
del persona1