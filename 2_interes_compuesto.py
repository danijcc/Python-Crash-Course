#Escribe un programa que calcule el área de un círculo con un radio = 5.
#Utiliza un valor aproximado de pi:

#######solucion 1##########
pi = 3.14
radius = 5
area = pi * radius ** 2 #forma 1 de representar potencia
print(f'Area: {area:.1f}')#:.1f formato de 2 decimales

#######solucion 2##########
radius = 5
pi = 3.14
resultado = pi * pow(radius ,2) #forma 2 de representar potencia
print(f'Area: {resultado}')

#####################################################################
#Escriba un programa que calcule el valor futuro de 1000 USD con una 
# tasa de interés anual del 3%, capitalización anual y un período de 
# inversión de 5 años. Redondea el resultado al centavo más cercano.
#####################################################################
#Formula de interés compuesto	P [(1 + R) n – 1]

p = 1000 #dolares
r = 3 #%
n = 5 #a;os
resultado = p * (1 + r/100) ** 5
print(f'El valor futuro de la inversión: {resultado:.2f}')#:.2f formato 2 decimales

#solucion 2
pv = 1000
r = 0.03
n = 5
fv = pv * (1 + r) ** n
print(f'The future value of the investment: {fv:.2f} USD')#:.2f formato 2 decimales