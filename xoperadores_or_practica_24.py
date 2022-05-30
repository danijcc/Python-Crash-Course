#video:4-operadores en python-> 9.-ejercicio operadores logicos

#en el siguiente ejercicio se ve si un padre puede asistir al juego de su hijo 
#si cualquiera de las 2 variables son verdaderas una u otra podra asistir al juego 
#esto lo evaluamos con el operador (or) 
vacaciones = False
diaDescanso = False

if vacaciones or diaDescanso:
    print ('puede aistir al juego')
else:
    print ('Tiene deberes por hacer')
