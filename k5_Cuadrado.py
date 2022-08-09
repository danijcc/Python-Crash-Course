#carpeta 12 video 2
from k3_herencia_multiple import FiguraGeometrica
from k4_Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #super().__init__(lado) el metodo super solo mandaria a llamar la primera clase padre 
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
