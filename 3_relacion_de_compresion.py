##########################################################
#                  RELACION DE COMPRESION 
#                    BY DANI COLMENARES
##########################################################
#   IN**3(pulgadas cubica) o CC(centimetros cubicos)
#                 1 IN**3 = 16,3871 CC
#                  STROKE = CARRERA DE PISTON
#               THICKNESS = ESPESOR DE LA EMPACADURA
# CONSTANTE O FACTOR FIJO = 0,7854
#                   CROWN = CORONA  
##########################################################
# V1 VOLUMEN DE CILINDRO
# V2 VOLUMEN DE LA CAMARA 
# V3 VOLUMEN DE LA EMPACADURA
# V4 VOLUMEN ENTRE PISTON Y BLOQUE (DTC PUNTO MUERTO SUPERIOR)
# V5 VOLUMEN CABEZA DEL PISTON
###########################################################
#   TODOS LOS RESULTADOS ESTAN EXPRESADOS EN IN**3
#----------------------------------------------------------
# FORMULA VOLUMEN DE CILINDRO:
# V1 = DIAMETRO DEL CILINDRO EN PULGADAS * DIAMETRO DEL CILINDRO EN PULGADAS * STROKE EN PULGADAS * 0,7854
#----------------------------------------------------------
# FORMULA VOLUMEN DE LA CAMARA:
# V2 CHAMBER = CC 
# 1 IN**3 = 16,3871 CC
# V2 = VOLUMEN DE LA CAMARA CC * 1 / 16,3871 
#----------------------------------------------------------
# FORMULA VOLUMEN DE LA EMPACADURA:
# V3 = DIAMETRO DE CILINDRO * DIAMETRO DE CILINDRO * ESPESOR DE LA EMPACADURA * 0,7854
#----------------------------------------------------------
# FORMULA VOLUMEN ENTRE PISTON Y BLOQUE DTC PUNTO MUERTO SUPERIOR
# V4 = DIAMETRO DE CILINDRO * DIAMETRO DE CILINDRO * VOLUMEN ENTRE PISTON Y BLOQUE * 0,7854
#----------------------------------------------------------
# FORMULA VOLUMEN CABEZA DEL PISTON
# DEPENDIENDO DEL PISTON SI ES TIPO DOMO = - O PLANO = + Y LAS ESPECIFICACIONES TECNICAS 
# DONDE NOS DIRA EL VALOR EN CC DEL ESPACIO QUE OCUPA EL PISTON EN LA CAMARA
# - 0 + V5 = VOLUMEN CABEZA DEL PISTON * 1 / 16,3871
###########################################################
# FORMULA RELACION DE COMPRESION PARA PISTON PLANO: 
# V1+V2+V3+V4+V5 / V2+V3+V4+V5 = RESULTADO RELACION DE COMPRESION
# FORMULA RELACION DE COMPRESION PARA PISTON TIPO DOMO: 
# V1+V2+V3+V4-V5 / V2+V3+V4-V5 = RESULTADO RELACION DE COMPRESION
###########################################################
print(f'''
############################################################################
                   GARAGE 7 SOFTWARE BY DANI COLMENARES
      INGRESE LOS SIGUIENTES VALORES PARA REALIZAR EL CALCULO RESPECTIVO
            PARA OBTENER LA RELACION DE COMPRESION POR PISTON
############################################################################
''')

valor1 = float(input(f'DIAMETRO DEL CILINDRO EN PULGADAS:....................................... '))
stroke = float(input(f'CARRERA O STROKE DEL PISTON EN PULGADAS:................................. '))
valor2 = float(input(f'VOLUMEN DE LA CAMARA EN CC:.............................................. '))
valor6 = float(input(f'DIAMETRO DE LA EMPACADURA EN PULGADAS:................................... '))
valor3 = float(input(f'ESPESOR O THICKNESS DE LA EMPACADURA EN PULGADAS:........................ '))
valor4 = float(input(f'ESPESOR ENTRE PISTON Y PUNTO MUERTO SUPERIOR EN PULGADAS:................ '))
valor5 = float(input(f'VOLUMEN DE LA CORONA O CROWN CABEZA DEL PISTON EN CC:.................... '))

v1 = valor1 * valor1 * stroke * 0.7854
v2 = valor2 * 1 / 16.3871 
v3 = valor6 * valor6 * valor3 * 0.7854
v4 = valor1 * valor1 * valor4 * 0.7854
v5 = valor5 * 1 / 16.3871

v1 = round(v1,4)
v2 = round(v2,4)
v3 = round(v3,4)
v4 = round(v4,4)
v5 = round(v5,4)

print(f'''
############################################################################
VOLUMEN DE CILINDRO:.............................................[{v1}]
VOLUMEN DE LA CAMARA:............................................[{v2}]
VOLUMEN DE LA EMPACADURA:........................................[{v3}]
VOLUMEN ENTRE PISTON Y BLOQUE DTC PUNTO MUERTO SUPERIOR:.........[{v4}]
VOLUMEN CABEZA DEL PISTON:.......................................[{v5}]
############################################################################
''')

volumen_de_la_camara_plano =  v2+v3+v4+v5
volumen_del_cilindro_plano =  v1+v2+v3+v4+v5 
volumen_de_la_camara_domo =  v2+v3+v4-v5
volumen_del_cilindro_domo =  v1+v2+v3+v4-v5 

resultado_piston_plano = volumen_del_cilindro_plano / volumen_de_la_camara_plano
resultado_piston_domo = volumen_del_cilindro_domo / volumen_de_la_camara_domo 

resultado_piston_plano = round(resultado_piston_plano,4)
resultado_piston_domo = round(resultado_piston_domo,4)

print(f'''
############################################################################
RELACION DE COMPRESION PARA PISTON FLAT O PLANO:................[{resultado_piston_plano} A 1]
RELACION DE COMPRESION PARA PISTON DOME O DOMO:.................[{resultado_piston_domo} A 1]
############################################################################

''')