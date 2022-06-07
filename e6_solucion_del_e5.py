#Carpeta 5: Video 7:
edad = int(input('proporciona tu edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'la infancia es increible...'
elif 10 <= edad < 20:
    mensaje = 'muchos cambios, mucho estudio...'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo...'
else:
    mensaje = 'Etapa de vida NO reconocida'
print(f'Tu edad es: {edad}, {mensaje}')