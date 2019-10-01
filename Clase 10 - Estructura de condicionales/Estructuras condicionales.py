def say_hello(age):
    if age > 18:
        print('Hola señor')
    else:
        print('Hola niño')

age = int(input('Digite la edad'))

if __name__ == '__main__':
    say_hello(age)