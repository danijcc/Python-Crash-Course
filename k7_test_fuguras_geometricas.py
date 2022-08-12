#carpeta 12 video 3,4,5,6
from k5_Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'rojo')
print(f'Calculo del area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)
#MRO - Method Resolution Order nos dice en que orden estamos mandando a llamar nuestros
#metodos padres

#print(Cuadrado.mro())
