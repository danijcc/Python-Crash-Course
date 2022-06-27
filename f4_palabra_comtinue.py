#Carpeta 6: Video 4:
#la funcion range define un rango
#la palabra continue  
# % = operador de modulo para determinar si la variable es divisible entre 2
#continue indica que se vaya a la siguiente iteracion y no ejecuta la lineas siguientes
# for i in range(6):
#     if i % 2 == 0:
#         print (f'Valor:{i}')

for i in range(6):
    if i % 2 != 0:  
        continue  
    print(f'Valor: {i}')
