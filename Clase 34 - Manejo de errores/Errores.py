countries = {
    'mexico': 122,
    'Colombia': 49,
    'Argentina': 43,
    'Chile': 18,
    'Perú': 31
}
while True:
    country = str(input('Escribe el nombre de un país: '))
    try:
        print('La población de {} son {} millones'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato de la población del país {}'.format(country))
    