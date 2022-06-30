#carpeta 7 video 1 y 2
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
#iterar lista se recomienda declarar la variable en singular y la loista en plural
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')
    