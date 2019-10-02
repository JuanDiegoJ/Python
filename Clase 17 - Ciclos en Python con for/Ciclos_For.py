#Muestra una secuencia en de número que va hasta el indice 5
print(list(range(5)))
#Muestra una secuencia que:
#1-Inicia en 5
#2-Termina en 40
#3-Da saltos en intervalos de 3 números
print(list(range(5,40,3)))
#Creación de un For que muestra los números del indice 1 al indice 5
for i in range(5):
    print(i)
#Creación de un for que si no cumple una condición ejecuta otra
for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i**2)
for i in range(30):
    if i % 3 == 0:
        print(i**2)
    elif i == 22:
        break
#Creación de un for que imprime cada letra de una palabra
r = 'ferrocarril'
for letter in r:
    print(letter)