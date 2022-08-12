#carpeta 12 video 2
from k3_FiguraGeometrica import FiguraGeometrica
from k4_Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        #super().__init__(lado) el metodo super solo mandaria a llamar la primera clase padre 
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def __str__(self):
        return  self.alto * self.ancho 

    def calcular_area(self):
        return self.alto * self.ancho
