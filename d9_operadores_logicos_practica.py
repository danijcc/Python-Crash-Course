#Carpeta:4-operadores en python-> 8.-ejercicio operadores logicos
valor = int(input('escribe el valor: '))
valorMinimo = 0
valorMaximo = 5
#entre parentesis tenemos una expresion booleana puedes utilizar o no los parentesis
#dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)
dentroRango = valor >= valorMinimo and valor <= valorMaximo

if dentroRango:
    print(f'El valor {valor} esta dentro de rango')
else:
    print(f'El valor {valor} esta fuera de rango')

