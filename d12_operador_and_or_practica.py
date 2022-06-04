#Carpeta:4-operadores en python-> 11.-ejercicio operadores logicos Rango entre 20's y 30's
edad = int(input('Introduce tu edad: '))

veintes = edad >= 20 and edad < 30
print(veintes)
treintas = edad >= 30 and edad < 40
print(treintas)

if veintes or treintas:
    #el back-slash o caracter de escape se escribe par aque no considere la comilla como caracter de cierre de la cadena
    print ('Dentro de rango (20\'s) o (30\'s)')
    if veintes:
        print ('dentro de los 20\'s')
    elif treintas:
        print ('Dentro de los 30\'s')
else:
    print("No esta dentro de los 20's no 30's ")