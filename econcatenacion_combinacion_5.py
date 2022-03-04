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

