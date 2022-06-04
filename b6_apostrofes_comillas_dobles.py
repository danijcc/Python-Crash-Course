#pag61->El apóstrofe aparece dentro de un conjunto de comillas dobles, por lo que el intérprete de Python
#no tiene problemas para leer la cadena correctamente:
message = "One of Python's strengths is its diverse community."
print(message)

#si usas comillas simple python no puede identificar donde termina el string saltando asi un error
#de sintaxis como en el  siguiente ejemplo:
#message = 'One of Python's strengths is its diverse community.'
#print(message)
#
# File "apostrophe.py", line 1
# message = 'One of Python's strengths is its diverse community.'
# 
# SyntaxError: invalid syntax
