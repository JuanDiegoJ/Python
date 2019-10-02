#Cadena
cadena = 'Juan Diego'
#Indica que cominza en la posición 1 y muestra el resto de la cadena
print(cadena[1:])
#Se le puede colocar un rango
print(cadena[0:3])
#Se le puede indicar al Slices que haga saltos dentro de la cadena
print(cadena[0:len(cadena):2])
#Se le puede indicar que muestre la palabra al revés
print(cadena[9:2:-1])
print(cadena[::-1])
#print(cadena[start:final:fases])