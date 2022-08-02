#carpeta 7 video 6
#un set agrega elementos en un orden aleatorio luego de agregado el dato no es posible
#modificarlo solo se pueden agagar datos nuevos o eliminar alguno ya existente

planetas={'Marte', 'jupiter', 'Venus'}
print(planetas)

#largo
print(len(planetas))

#revisar si un elemnto esta presente en la coleccion set
print('Martes' in planetas)
 
#agregar un elemento a la variable planetas mediante un metodo llamado .add() 
planetas.add('Tierra')
print(planetas)

#set nos puede servir para no tener elemntos duplicados en una lista de datos
#asi lo intentemos dulicar solo tendremos un elemento 
planetas.add('Tierra')
print(planetas)

#eliminar elementos
planetas.remove('Tierra')
print(planetas)

#eliminar elemento sin arrojar error en caso que no se encuentre el elemento descrito
planetas.discard('jupiters')
print(planetas)

#limpiar set 
planetas.clear()
print(planetas)

#eliminar la variable set por completo
del planetas
