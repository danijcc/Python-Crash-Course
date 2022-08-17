#carpeta video 3,4,5,6,7,8,9
#herencia multiple se refiere basicamente a que una clase hija o subclase puede heredar
# de multiples clases padres 
#clase abc = abstract base class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho): #validamos si el ancho es mayor que 0 y menor que 10
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')
        if self._validar_valor(alto):  
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo alto: {alto}')
    @property 
    def ancho(self): #este es un metodo get
        return self._ancho
       
    @ancho.setter#este es un metodo set
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo Ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'valor erroneo del alto:{alto}')

    @abstractmethod #decorador 
    def calcular_area(self):
        pass


    def __str__(self):
        return  f'FiguraGeometrica: [Ancho: {self._ancho}, Alto: {self._alto}]' 

    def _validar_valor(self,valor):#funcion validar 
        return True if 0 < valor < 10 else False