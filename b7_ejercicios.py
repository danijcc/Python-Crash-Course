# 1.-Guarde el nombre de una persona en una variable e imprima un mensaje.
# de esa persona. Su mensaje debe ser simple, como, "Hola Dani,
# ¿Te gustaría aprender algo de Python hoy?”

first_name = "Dani"
print("Hola " + first_name + "¿Te gustaría aprender algo de Python hoy?")

#2.-Almacene el nombre de una persona en una variable y luego imprima el nombre persona.
# en minúsculas, mayúsculas y título.

first_name = "dani"
print(first_name.upper())
print(first_name.lower())
print(first_name.title())

#3.- Encuentra una cita de una persona famosa que admires. Imprime el
# cita y el nombre de su autor. Su salida debe parecerse a la
# siguiente, incluyendo las comillas:
# Albert Einstein dijo una vez:, “Una persona que nunca haya cometido un
# error nunca provee nada nuevo.”

quote="Albert Einstein once said, “A person who never made a mistake never tried anything new.”"
print(quote)

# Repita el ejercicio 2, pero esta vez almacene el nombre de la persona famosa en una variable 
# llamada persona_famosa. Luego redacta tu mensaje
# y almacenarlo en una nueva variable llamada mensaje. Imprime tu mensaje.

famous_person="Albert Einstein"
message=" once said, “A person who never made a mistake never tried anything new.”"
print(famous_person + message)

# Almacene el nombre de una persona e incluya algunos espacios en blanco
# caracteres al principio y al final del nombre. Asegúrese de usar cada
# combinación de caracteres, "\t" y "\n", al menos una vez.
# Imprima el nombre una vez, de modo que se muestre el espacio en blanco alrededor del nombre.
# Luego imprima el nombre usando cada una de las tres funciones de eliminación, lstrip(),
# rstrip() y strip().

name = " \n\tDani  "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())