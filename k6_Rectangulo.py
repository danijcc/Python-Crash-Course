#carpeta 12 video 3,4,5,6,7
from k3_FiguraGeometrica import FiguraGeometrica
from k4_Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        #super().__init__(lado) el metodo super solo mandaria a llamar la primera clase padre 
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
    
    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return  f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'


