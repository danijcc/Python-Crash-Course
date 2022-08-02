#carpeta 9 video 11,12
class Rectangulo:#recomentable iniciar la clase con letra mayuscula
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calrcular_area(self):
        return self.base * self.altura


base = int(input('proporciona la base: '))
altura = int(input('proporciona la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'Area rectangulo: {rectangulo1.calrcular_area()}')


