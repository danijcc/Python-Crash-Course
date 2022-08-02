#carpeta 9 video 9,10
class Aritmetica:
    """
    Clase aritmetica para realizar las operaciones sumar, restar, etc.
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA #2 self.atributo = parametro recibido 
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA -  self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7,9) #1
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicacion: {aritmetica1.multiplicar()}')
print(f'Division: {aritmetica1.dividir():.2f}')#:.2f indica cuantos caracteres flotantes queremos que muestre