#un diccionario{} esta compuesto por una llave y un valor = dict (key, value)
#un diccionario es parecido a un set ya que no tiene indices para acceder a el
#para acceder a el se utiliza directamente la llave (key)
#y no se puedre agregar registros duplicados
#carpeta 7 video 7 y 8
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)

#para conocer el largo de los elementon de nuestro diccionario pasamos la funcion print luego leng
print(len(diccionario))

#acceder a un elemento (key)
print(diccionario['IDE'])

#otra forma de recuperar un elemento usamos nuevamente la funcion print y luego la funcion get
print(diccionario.get('OOP'))

#modificando elementos
diccionario['IDE']='Entorno de Desarrollo Integrado'
print(diccionario)

#recorrer los elementos utilizando la funcion items()para devolver termino y valor
for termino, valor in diccionario.items():
    print(termino,  valor)

#recorrer solo para recuperar las llaves con la funcion keys()
for llaves in diccionario.keys():
    print(llaves)

#recorrer solo para recuperar el valor con la funcion values()
for valor in diccionario.values():
    print(valor)

#comprobar existencia de algun elemento en el diccionario
print ("Is value IDE in the diccionario?", 'IDE' in diccionario)

#agregar un elemento de la variable diccionario
diccionario ['Pk'] ='Primary Key'
print (diccionario)

#remover un elemento de la variable diccionario
diccionario.pop('DBMS')
print(diccionario)

#limpiar la variable diccionario
diccionario.clear()
print(diccionario)

#eliminar la variable de diccionario
del diccionario
print(diccionario)