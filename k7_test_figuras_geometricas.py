#carpeta 12 video 3,4,5,6,7,8,9
from k3_FiguraGeometrica import FiguraGeometrica
from k5_Cuadrado import Cuadrado
from k6_Rectangulo import Rectangulo

#No se puede instanciar una clase abstracta
#figura = FiguraGeometrica()

print('Creacion objeto Cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f'Calculo del area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creacion objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=3, alto=8, color='verde')
print(f'Calculo area Rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#MRO - Method Resolution Order nos dice en que orden estamos mandando a llamar nuestros
#metodos padres

print(Cuadrado.mro())
