def run():
    counter = 0
    with open('leer.txt') as f:
    #Cuando se ejecuta readlines(), convierte el archivo en una lista
    #Divide el texto en diferentes String cuando termina una línea
        for line in f:
            counter += line.count('Beatriz')
    print('Beatriz se encuentra {} en el texto'.format(counter))


if __name__ == '__main__':
    run()