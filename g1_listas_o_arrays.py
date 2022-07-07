#carpeta 7 video 1, 2 y 3
from turtle import clear
nombres = ['juan','karla','ricardo','maria']
#imprimir la lista nombres
print (nombres)
#acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])
#acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2])#sin uncluir el indice 2
#ir del inicio de la lista al indice 3 (sin incluirlo)
print(nombres[:3])
#desde el indice indicado hasta el ultimo
print(nombres[0:])  
#cambiar valor 
nombres[3] = 'ivone'
print (nombres)
#iterar lista se recomienda declarar la variable en singular y la lista en plural
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')
#preguntar el largo de una lista
print (len(nombres))
#insertar un elemento en un indice en especifico
nombres.insert(1,'octavio')
print(nombres)
#remover un elemento
nombres.remove('octavio')
print(nombres)
#remover el ultimo valor agragado
nombres.pop()
print(nombres)
#eliminar un indice
del nombres[0]
print(nombres)
#limpar la lista
nombres.clear()
print(nombres)
#borrar la lista por completo
del nombres 
print(nombres)
