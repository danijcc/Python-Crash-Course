
# Cada variable tiene un valor, que es la información asociada o almacenada a esa variable.
# Cuando procesa la primera línea, asocia el texto "¡Hola, mundo de Python!"
# con el mensaje variable. Cuando llega a la segunda línea, imprime el valor
# asociado con el mensaje a la pantalla.

# REGLAS PARA NOMBRAR VARIABLES

# 1.-Los nombres de variables solo pueden contener letras, números y guiones bajos.
# Pueden comenzar con una letra o un guión bajo, pero no con un número.
# Por ejemplo, puede llamar a una variable mensaje_1 pero no a 1_mensaje.
# nota personal mejor usar camel case y que la variable sea autodescriptiva

# 2.-No se permiten espacios en los nombres de variables, pero se pueden usar guiones bajos
# para separar palabras en nombres de variables. Por ejemplo, greeting_message funciona,
# pero el mensaje de saludo causará errores.

# 3.-Evite usar palabras reservadas de Python y nombres de funciones como nombres de variables;
# es decir, no use palabras que Python ha reservado para un pro-
# propósito gramatical, como la palabra print. (Consulte “Palabras clave o reservadas de Python
# y funciones integradas” en la página 489.)

# Los nombres de las variables deben ser breves pero descriptivos. Por ejemplo, el nombre es
# mejor que n, nombre_estudiante es mejor que s_n y longitud_nombre es mejor
# que length_of_persons_name.

# Tenga cuidado al usar la letra minúscula l y la letra mayúscula O
# porque podrían confundirse con los números 1 y 0.

variableDeControl = "variable definida"
print(variableDeControl)
variableDeControl = "misma variable redefinida"
print(variableDeControl)

miVariable = "hola desde Python"
print (miVariable)

#Enteros
x = 10
y = 2
z = x + y
print(z)

#Direcciones de memoria o posisiones de memoria las literales 
# se almacenan en una direccio de memoria la recuperamos mediante la funcion id()
print (id(x))

