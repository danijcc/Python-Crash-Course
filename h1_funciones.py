#una funcion es un bloque de codigo que podemos llamar x cantidad de veces
#la palabra reservada def sirve para definir dicha funcion
#una vez definida o declarada la funcion por medio de los parentesis esta  
#recibira los parametros con la cual esta funcionara
#carpeta 8 video 1, 2, 3, 4, 5, 6, 7 y 8

def mi_funcion():  
    print('saludos desde mi funcion nro1') 
#debemos llamar la funcion
mi_funcion()
mi_funcion()
#####################################################################

def mi_funcion(nombre, apellido): #2 estos parentesis reciben parametros 
                                  #mediante las variables que declaremos
                                  #en nuestra funcion
    print('saludos desde mi funcion') 
    print(f'Nombre: {nombre}, Apellido: {apellido}')#3
#debemos llamar la funcion
mi_funcion('Juan','Perez')#1 estos parentesis envian argumentos o parametros
                          #a las variable de nuestra funcion
                         
################################################################################
def sumar (a,b): #2 parametros = variables de nuestra funcion
    return a + b #3 con return vamos a regresar la suma de a + b

resultado = sumar(2,2)  #1-4 argumentos = valores enviados a las variables de
                        #nuestra funcion
print(f'Resultado de la suma es: {resultado}')#5 
print(f'Resultado de la suma es: {sumar(2,2)}')#5 

####################valores por defecto############################################
def sumar (a = 0,b = 0) -> int: # parametros por defecto es 0 para las variables a y b
                                #(-> int) solo es un pista opcional del valor que regresara
                                # la funcion ya que los tipos de datos en python son dinamicos
    return a + b # con return vamos a regresar la suma de a + b
resultado = sumar()#aca llamamos la funcion sin mandar ningun argumento
print(f'Resultado de la suma es: {resultado}')#default
print(f'Resultado de la suma es: {sumar(2,8)}')#aca mandamonos argumentos
##################################################################################
#pasar varios parametros , args o tupla a la funcion en la doc esta como args
def listarNombres(*nombres):#se antepone el * para indicar que vamos a pasar varios 
                            #parametros o args a la misma funcion internamente python lo 
                            #manejara como una tupla
    for nombre in nombres:#aca lo iteramos como si fuera una tupla
        print(nombre)

listarNombres('juan', 'Karla','Maria','Ernesto')
##################################################################################
#pasar un diccionario llave-valor como argumento o parametro en la doc esta como
#kwargs aunque podemos escribir el nombre que mas nos guste 
def listarTerminos (**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')

listarTerminos(IDE='Integrated Development Environment',PK='Primary Key')
listarTerminos(DBMS='Database Management System')
###################################################################################
#esta funcion recibe una lista
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan','Karla','Guillermo']
desplegarNombres(nombres)#tenemos una tupla iterable
desplegarNombres('Carlos')#tenemos un nombre que tambien es iterable sus letras
desplegarNombres((10,11))#para iterar un valor entero debe convertirse en una tupla
desplegarNombres([10,11])#para iterar un valor entero debe convertirse en una lista
#################################################################################
#funcion recursiva es aquella que se manda a llamar a si misma para completar
#una tarea en el siguiente ejemplo sirve para obtener el factorial de cierto numero
#5 = 5 * 4 * 3 * 2 * 1
#5 = 5 * 4 * 3 * 2
#5 = 5 * 4 * 6 
#5 = 5 * 24
#5 = 120
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial (numero-1)

resultado = factorial(5)
print(f'El factorial de 5 es {resultado}')








