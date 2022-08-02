class Rectangulo: #recomentable iniciar la clase con letra mayuscula
    def __int__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):    
        return self.base * self.altura  
        
base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))

rectangulo1 = Rectangulo(base,altura)
print(f'El area es: {rectangulo1.calcular_area()}')
