#un diccionario esta compuesto por una llave y un valor = dict (key, value)
#un diccionario es parecido a un set ya que no tiene indices para acceder a el
#para acceder a el se utiliza directamente la llave (key)
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