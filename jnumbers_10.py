# Numeros Enteros:
# Pueden sumar (+), restar (-), multiplicar (*) y dividir (/) enteros en Python
# 1 / 5
# 2 + 3
# 3 - 2
# 2 * 3

# En una sesión de terminal, Python simplemente devuelve el resultado de la operación.
# Python usa dos símbolos de multiplicación para representar exponentes:
# >>> 3 ** 2
# 9
# >>> 3 ** 3
# 27
# >>> 10 ** 6
# 1000000

# Python también admite el orden de las operaciones, por lo que puede usar múltiples
# operaciones en una expresión. También puede usar paréntesis para dar prioridad al
# orden de operaciones para que Python pueda evaluar una expresión en el orden
# que tu específicas. Por ejemplo:
# >>> 2 + 3*4
# 14
# >>> (2 + 3) * 4
# 20
# El espaciado en estos ejemplos no tiene efecto en cómo Python evalúa
# las expresiones; simplemente le ayuda a detectar más rápidamente las operaciones que
# tienen prioridad cuando estás leyendo el código.

# Flotantes:
# Python llama flotante a cualquier número con un punto decimal. Este término se usa en
# la mayoría de los lenguajes de programación, y se refiere al hecho de que un punto decimal
# puede aparecer en cualquier posición en un número. Todo lenguaje de programación debe
# estar cuidadosamente diseñado para administrar correctamente los números decimales, de modo que los números
# deberia comportarse apropiadamente sin importar dónde aparezca el punto decimal.
# En su mayor parte, puede usar decimales sin preocuparse de cómo
# Ellos se comportan. Simplemente ingrese los números que desea usar y Python
# lo más probable es que haga lo que espera:
# >>> 0.1 + 0.1
# 0.2
# >>> 0.2 + 0.2
# 0.4
# >>> 2 * 0.1
# 0.2
# >>> 2 * 0.2
# 0.4
# Pero tenga en cuenta que a veces puede obtener un número arbitrario en vez 
# del resultado esperado:
# >>> 0.2 + 0.1
# 0.30000000000000004
# >>> 3 * 0.1
# # 0.30000000000000004
# Esto sucede en todos los idiomas y es de poca importancia. Pytho intenta
# encontrar una manera de representar el resultado con la mayor precisión posible, lo que a
# veces es difícil dada la forma en que las computadoras tienen que representar números 
# internamente.Sólo ignore los caracteres decimales adicionales por ahora; aprenderás maneras de lidiar con el
# lugares adicionales cuando lo necesite en los proyectos de la Parte II.
# ################################################################################

# age=23
# message="feliz"+age+"cumpleaños"
# print(message)

# Traceback (most recent call last):
#   File "/home/cadiz/Escritorio/python_work/jnumbers_10.py", line 58, in <module>
#     message="feliz"+age+"cumpleaños"
# TypeError: can only concatenate str (not "int") to str

# Este es un error de tipo. Significa que Python no puede reconocer el tipo de información
# que está usando. En este ejemplo, Python ve que estás usando una variable
# que tiene un valor entero (int), pero no está seguro de cómo interpretar ese
# valor. Python sabe que la variable podría representar el valor numérico
# 23 o los caracteres 2 y 3. Cuando usa números enteros dentro de cadenas
# así, debe especificar explícitamente que desea que Python use la enteros
# como una cadena de caracteres. Puede hacer esto envolviendo la variable en el
# función str(), que le dice a Python que represente valores que no son cadenas como cadenas:

age=23
message="feliz "+str(age)+" Cumpleaños"
print(message)

