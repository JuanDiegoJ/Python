#Programa para adivinar un número
#Importar el módulo
import random
def number_sc():
    number_int=int(input('¿Desde qué número es la búsqueda?'))
    return int(number_int)
def run():
    number_found = False
    number_input = number_sc()
    random_number = random.randint(0,number_input)

    while not number_found:
        number = int(input('intenta un número: '))

        if number == random_number:
            print('Felicidades. Encontraste el número')
            number_found = True
        elif number > random_number:
            print('El número es más pegueño')
        else:
            print('El número es más grande')

if __name__ == '__main__':
    run()

#Imprime los números del 1 al 10
#i = 0
#while i < 10:
#    print(i)
#    i += 1
#j = 0
#Muestra de un Loop infinito
#while j >= 0:
#    print(j)
#    j += 1




