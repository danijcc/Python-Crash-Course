#evalua la exprecion numerica para saber si es par o impar
a = int(input('escribe un valor numerico:'))

#print (a % 2)

if a % 2 == 0:
    print (f'el valor de "a" {a} es par')
else:
    print (f'el valor de "a" {a} es impar')