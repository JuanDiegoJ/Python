#Método de conversión de pesos mexicanos a colombianos
def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97
    return mex_to_col_rate * ammount

#Método dónde comienza el programa
def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos mexicanos a pesos colombianos')
    print('')
    #Captura la cantidad de pesos mexicanos
    ammount = float(input('Ingrese la cantidad de pesos ' +
     'mexicanos que desee convertir'))
    #Resultado de ejecutar el metodo de convertir pesos mexicanos a colombianos
    #Se pueden asignar variables a métodos
    result = foreign_exchange_calculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))
    print('')

#Indica desde dónde comienza a ejecutar Python el programa
if __name__ == '__main__':
    run()