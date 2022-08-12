#carpeta 12 video 1
class Color:
    def __init__(self, color):
        self.color = color

    @property 
    def color(self): #este es un metodo get
        print('llamando metodo get color')
        return self._color
       
    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return  f'Color: [Color: {self._color}]'     