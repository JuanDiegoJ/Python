#Modelo de una lampara
#Para definir una clase se usa el KeyWord 
#Las clases se inician en mayúsculas
class Lamp:
    _LAMPS=['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']
    """Siempre se tiene que iniciar este método, todas las clases en
    Python tienen que recibir este parámetro que es la propia instancia"""
    #Este es el método constructor
    #Se definen las variables
    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on
    #Turn_on y turn off cambian el estado de la imagen
    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

