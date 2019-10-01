def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else: 
        for i in range(3, number):
            if number % i == 0:
                return False
            
    return True

def run():
    #Cuando la función está vacía se coloca la keyword pass para que
    # Python sepa cuándo termina la función 
    number = int(input('Escribe un número: '))
    result = is_prime(number)
    if result == True:
        print('El número es primo')
    else:
        print('El número no es primo')
    pass

if __name__ == '__main__':
    run()