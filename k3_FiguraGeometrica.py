#carpeta 12 video 1
#herencia multiple se refiere basicamente a que una clase hija o subclase puede heredar
# de multiples clases padres 
class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property 
    def ancho(self): #este es un metodo get
        return self._ancho
       
    @ancho.setter#este es un metodo set
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def __str__(self):
        return  f'FiguraGeometrica: [Ancho: {self._ancho}, Alto: {self._alto}]' 