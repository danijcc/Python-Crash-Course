FACTOR_FIJO = 0.7854
valor1 = float(input(f'DIAMETRO DEL CILINDRO EN PULGADAS: '))
stroke = float(input(f'CARRERA DEL PISTON EN PULGADAS: '))

v1 = valor1 * valor1 * stroke * FACTOR_FIJO


print(f'''
{v1}
''')