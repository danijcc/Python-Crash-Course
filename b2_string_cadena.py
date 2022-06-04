# En este ejemplo, la cadena en minúsculas "dani colmenares" se almacena en la variable
# name El método title() aparece después de la variable en el estado print() o funcion print().
# Un método es una acción que Python puede realizar en un dato. el
# punto (.) después del nombre en name.title() le dice a Python que haga el método title()
# actuar sobre el nombre de la variable. Cada método va seguido de un conjunto de paréntesis,
# porque los métodos a menudo necesitan información adicional para hacer su trabajo.
# Esa información se proporciona entre paréntesis. La función títle()
# no necesita ninguna información adicional, por lo que sus paréntesis están vacíos.
# title() muestra cada palabra en mayúsculas y minúsculas, donde cada palabra comienza con un
# letra mayúscula. 

name = "dani colmenares"
print(name.title())


##################################################################################
# Esto es útil porque a menudo querrá pensar en un nombre como un
# pieza de información. Por ejemplo, es posible que desee que su programa reconozca
# los valores de entrada Dani, DANI y dani como el mismo nombre, y muestre todos
# ellos como Dani.
# Varios otros métodos útiles están disponibles para tratar el caso también.
# Por ejemplo, puede cambiar una cadena a letras mayúsculas o minúsculas.

#########################################################################################
# Varios otros métodos útiles están disponibles para tratar el caso también.
# Por ejemplo, puede cambiar una cadena a letras mayúsculas o minúsculas.
# ejemplo:
name = "dani  colmenares"
print(name.upper())
print(name.lower())

#########################################################################################
#GLOSARIO

#METODO->Se le llama a un bloque de código que tiene definido en su 
# interior un conjunto de instrucciones o subrutinas, estas instrucciones realizan una determinada tarea. 
# Cuando se necesita hacer uso de la función definida en el método simplemente se lo llama por 
# su nombre, cuando el flujo del programa pasa por una llamada a un método el puntero salta a 
# la región donde está definido el método, ejecuta todas sus instrucciones y al finalizar retorna
# a la línea posterior a la llamada al método.

#FUNCION->Se le llama a un bloque de código que tiene definido en su 
# interior un conjunto de instrucciones o subrutinas, estas instrucciones realizan una determinada tarea. 
#
#FUERA DE UNA CLASE -> DEVUELVE RESULTADO -> FUNCION
#DENTRO DE UNA CLASE -> DEVUELVA O NO  RESULTADO -> METODO
#