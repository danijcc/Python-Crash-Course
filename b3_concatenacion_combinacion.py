# Combinación o concatenación de cadenas:
# A menudo es útil combinar cadenas. Por ejemplo, es posible que desee almacenar
# un nombre y un apellido en variables separadas, y luego combinarlos
# cuando desea mostrar el nombre completo de alguien:
# Python usa el símbolo más (+) para combinar cadenas. En este ejemplo,
# usamos + para crear un nombre completo combinando un first_name , un espacio y un
# last_name , dando este resultado:

first_name = "dani"
last_name = "colmenares"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
message = ("Hello, " + full_name.title() + "!")
print(message)

#FORMA 1 DE CONCATENAR CADENAS
miGrupoFavorito = "Nightwish" +" "+ "the best rock band"
print("mi grupo favorito es: " + miGrupoFavorito)

#FORMA 2 DE CONCATENAR CADENAS
miGrupoFavorito = "Nightwish" 
comentario = "the best rock band"
print("mi grupo favorito es:", miGrupoFavorito, comentario)

# funcion int() convierte la variable a un tipo entero 
numero1 = "1"
numero2 = "2"
print ("Concatenacion", numero1 + numero2)
print("Suma:", int(numero1) + int (numero2))

