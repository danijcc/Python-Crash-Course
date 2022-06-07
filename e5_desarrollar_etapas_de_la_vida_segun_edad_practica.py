#Carpeta 5: Video 6:
edad = int(input('proporciona tu edad: '))
etapa = None

if edad >= 0 and edad <= 10:
    etapa = 'La infancia es increible...'
elif edad >= 11 and edad <= 20:
    etapa = 'Muchos cambios y mucho estudio...'
elif edad >= 21 and edad <= 30:
    etapa = 'Amor y comienza el trabajo...'
else:
    etapa = 'Etapa de vida no reconocida'
print(f'para la edad de {edad} a;os la etapa de la vida es {etapa}')