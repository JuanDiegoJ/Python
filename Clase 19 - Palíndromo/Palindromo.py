#Método para comprobar la palabra con Slice
def palindrome2(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False
#Método para comprobar la palabra con listas
def palindrome(word):
    reversed_letters = []
    for letter in word:
        reversed_letters.insert(0, letter)
    reversed_word = ''.join(reversed_letters)
    if reversed_word == word:
        return True
    else:
        return False
#Ejecuta el programa
if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))
    result = palindrome2(word)
    if result == True:
        print('{} Sí es un palíndormo'.format(word))
    else:
        print('{} No es un palíndromo'.format(word))