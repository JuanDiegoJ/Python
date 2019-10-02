def average_temps(temps):
    sum_of_temps = 0
    for temp in temps:
        sum_of_temps += float(temp)
    return sum_of_temps / len(temps)

if __name__ == '__main__':
    temps = [21, 24, 26, 22, 20, 23, 24]

    average = average_temps(temps)
    #Imprime el valor con todos los decimales
    print('La temperatura promedio es: {}'.format(average))
    #Imprime el valor aproximando
    print('La temperatura promedio es: {}'.format(round(average)))
    #Imprime el valor aproximando con cierto número de decimales
    print('La temperatura promedio es: {}'.format(round(average,2)))