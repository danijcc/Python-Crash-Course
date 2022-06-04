# En el siguiente ejercicio se solicita calcular el área y el perímetro de un Rectángulo, 
# para ello deberemos crear las siguientes variables:

# alto (int)

# ancho (int)

# El usuario debe proporcionar los valores de largo y ancho, y después se debe imprimir 
# el resultado en el siguiente formato(no usar acentos y respetar los espacios, mayúsculas, minúsculas 
# y saltos de línea):

# Proporciona el alto:
# Proporciona el ancho:
# Area: <area>
# Perímetro: <perimetro>
# Las fórmulas para calcular el área y el perímetro de un Rectángulo son:

# Área: alto * ancho

# Perímetro: (alto + ancho) * 2

# Nota: Recordar que las tareas no cambian de estado y no afectan en el avance de tu curso ni en 
# la generación de tu certificado de finalización del curso en Udemy.

# Preguntas de esta tarea
# ¿Cuál es el código del requerimiento solicitado?

#Mi respuesta
alto = input('Proporciona el alto:')
ancho = input('Proporciona el ancho:')
area = int(alto) * int(ancho)
perimetro = (int(alto) + int(ancho)) * 2
print(f'El area es {area}')
print(f'El perimetro es {perimetro}')

#respuesta del curso
alto = int(input("Proporciona el alto del rectángulo:"))
ancho = int(input("Proporciona el ancho del rectángulo:"))
     
area = alto * ancho;
perimetro = (alto + ancho) * 2;
print("Área:", area);
print("Perímetro:", perimetro);