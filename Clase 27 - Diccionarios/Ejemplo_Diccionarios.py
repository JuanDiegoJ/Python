calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matemáticas'] = 10
calificaciones['web'] = 8
calificaciones['bases de datos'] = 10

for key in calificaciones:
    print(key)
for value in calificaciones.values():
    print(value)
for key,value in calificaciones.items():
    print('llave: {}, valor {}'.format(key, value))
suma_de_calificaciones = 0
for calificacion in calificaciones.values():
    suma_de_calificaciones += int(calificacion)

print(suma_de_calificaciones/len(calificaciones.values()))