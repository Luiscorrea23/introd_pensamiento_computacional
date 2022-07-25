#Programación defensiva
#Alternativa a print statement 

# def comprueba_si_es_una_palabra(palabra):
#     caracteres = []

#     for caracter in palabra :
#         print(caracter)
#         assert type(caracter) == str, f" {palabra}: No es una palabra"
#         assert len(caracter) > 0, "La palabra no tiene caracteres o str vacio"

#         caracteres.append(caracter)

# test = comprueba_si_es_una_palabra(range(10))
# print(test)

from ast import Str


class Mi_Excepcion_Personalizada(Exception):
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2


def comprueba_si_es_una_palabra(palabra):
    
    try:
        assert type(palabra) == str, "no es una palabra"
        assert len(palabra) >0, "la cadena esta vacia"
  
    except TypeError as e:
        print(e)
        return "No es una palabra"

test = comprueba_si_es_una_palabra(0)
print(test)

# def primera_letra(lista_palabras):
#     primeras_letras = []
    
#     for palabra in lista_palabras:
#         try:
#             assert type(palabra) == str, f'{palabra} no es String'
#             assert len(palabra) > 0 , 'No se permiten vacios'
#             primeras_letras.append(palabra[0])
#         except AssertionError as e:
#             print(e)

#     return primeras_letras


# lista = ['Angelo',5.5, '', 2 , '43952353', 0.35]
# print('Primeras letras validas son : ' , primera_letra(lista))
