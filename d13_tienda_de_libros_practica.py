#Carpeta 4: video 12: ejercicio a desarrollar tienda de libros 
print('Proporciona los siguientes datos del libro')
Nombre = input('Proporcionar el Nombre: ')
Id = int(input('Proporcionar el Id: '))
Precio = float(input('Proporcionar el Precio: '))
Envio = input('Indica El Envio es Gratuito: ')

#si se cumple la siguiente condicion
if Envio == 'True':
#se ejecuta esto
    Envio = True
#si no se cumple se ejecuta esto o de lo contrario
elif Envio == 'False':
    Envio = False 
#entonces de no cumplirse ninguna de las anteriores se ejecutara esta
else:
    Envio = 'Valor incorrecto, debe escribir True/False'

print(f'''
Nombre:{Nombre}
Id:{Id}'
Precio:{Precio}
Envio:{Envio}
''')
 