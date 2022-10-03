#----------------------------------------------------------------------------
#FORMULA EMPLEADA DESPLAZAMIENTO ANGULAR 
#0 = 1/2 * a * t**2
#a = 1 rad/s**2 aceleracion angular
#0 = ? ->DESPLASAMIENTO ANGULAR
#t = input ->tiempo 
#----------------------------------------------------------------------------
#1 RADIAN ES 57.33 GRADOS = ES LA MEDIDA DE UN ANGULO CENTRAL Y LA LONGITUD DEL
#ARCO SUBTENDIDO ES IGUAL A SU RADIO (EL RADIO Y EL ARCO MIDAN LOS MISMO )
#360 GRADOS ES IGUAL A 6.62 RADIANES

RADIAN = 57.33
VUELTA = 360

tiempo =int(input("INGRESE EL TIEMPO EN SEGUNDOS: "))
aceleracion_angular_sensor_distribuidor=float(input("INGRESE ACELERACION DEL DISTRIBUIDOR RAD/S**2: "))
aceleracion_angular_sensor_cigueñal=float(input("INGRESE ACELERACION DEL CIGUEÑAL RAD/S**2: "))


resultado_tiempo = tiempo **2
aceleracion_angular_sensor_distribuidor
aceleracion_angular_sensor_cigueñal

desplazamiento_angular_del_distribuidor = 1/2 * resultado_tiempo * aceleracion_angular_sensor_distribuidor
desplazamiento_angular_del_cigueñal = 1/2 * resultado_tiempo * aceleracion_angular_sensor_cigueñal

nro_de_vueltas_del_cigueñal = desplazamiento_angular_del_distribuidor * RADIAN / 360
nro_de_vueltas_del_distribuidor = desplazamiento_angular_del_cigueñal * RADIAN / 360

posicion_del_cigueñal_en_grados = 360 / nro_de_vueltas_del_cigueñal 
posicion_del_distribuidor_en_grados = 360 / nro_de_vueltas_del_distribuidor

print(f'''\nEL DESPLAZAMIENTO ANGULAR DEL CIGUEÑAL ES {desplazamiento_angular_del_cigueñal} RADIANES,
 EL NUMERO VUELTAS ES {nro_de_vueltas_del_cigueñal} Y LA POSICION ES {posicion_del_cigueñal_en_grados} 
GRADOS POR CADA {tiempo} SEGUNDOS \n ''' )
print(f'''EL DESPLAZAMIENTO ANGULAR DEL DISTRIBUIDOR ES {desplazamiento_angular_del_distribuidor} RADIANES,
EL NUMERO VUELTAS ES {nro_de_vueltas_del_distribuidor} Y LA POSICION ES {posicion_del_distribuidor_en_grados}
GRADOS POR CADA {tiempo} SEGUNDOS''')
