#Carpeta 5: Video 5:
#segun el mes proporcionado del 1 al 12 establecer la estacion a que pertenece dicho mes
#primavera,verano,oto;o,invierno
mes = int(input('proporciona mes del a;o (1-12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'oto;o'
else:
    estacion = 'mes incorrecto'
print(f'para el mes {mes} la estacion es {estacion}')