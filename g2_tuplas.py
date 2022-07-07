#carpeta 7 video 4 y 5
#una tupla basicamente es una lista que no se puede modificar es inmutable
frutas = ('manzana','pera','uva','fresa')
print(frutas)
#saber el largo de una tupla
print(len(frutas))
#acceder a un elemento de la tupla
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#acceder a un rango de elementos de la tupla
print(frutas[0:1])#sin incluir el ultimo indice
#si la tupla solo tiene un elemento debemos colocal una coma al final
frutaUnica = ('manzana',)
print(frutaUnica)

#recorrer elementos de una tupla
for fruta in frutas:
    print(fruta, end=' ')

#cambiar de tupla a lista para modificar un valor
frutasLista = list(frutas)
frutasLista[0] = 'mandarina'
frutas = tuple(frutasLista)
print('\n',frutas)

#eliminar la tupla por completo
del frutas
print(frutas)



