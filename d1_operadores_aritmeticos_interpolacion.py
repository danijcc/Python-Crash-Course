#addition         +
#subtraction      -
# multiplication  *
#division         /
#integer division // no utiliza punto flotante regresa un valor entero siempre
#exponention      **
#modulo/remainder % resuduo de la division

operandoA = 3
operandoB = 2
suma = operandoA + operandoB
print('Resultado de la suma ',suma )
#otra forma de imprimir es con f literal a esto se le 
#llama interpolacion (incluir variables en una cadena)
print(f'Resultado de la suma: {suma} ') 
#resta
resta = operandoA - operandoB
print(f'resultado resta: {resta}')
#multiplicacion
multiplicacion = operandoA * operandoB
print(f'Resultado multiplicacion {multiplicacion}')
#division
division = operandoA / operandoB
print(f'Resultado division {division}')
divisionint = operandoA // operandoB
print(f'Resultado division enteros: {divisionint}')
#modulo
modulo = operandoA % operandoB
print(f'Resultado residuo division (modulo): {modulo}')
#exponente
exponente = operandoA ** operandoB
print(f'Resultado exponente: {exponente}')
