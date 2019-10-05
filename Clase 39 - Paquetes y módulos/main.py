from lamp import Lamp

def run():
    lamp = Lamp(is_turned_on = False)

    while True:
        comand = str(input('''
        ¿Qué deseas hacer?
        [p]render
        [a]apagar
        [s]alir
        '''))

        if comand == 'p':
            lamp.turn_on()
        elif comand == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == '__main__':
    run()