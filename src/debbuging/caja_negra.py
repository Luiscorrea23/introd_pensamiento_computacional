#Pruebas de caja negra 
#No conocemos el codigo o la implementación
#vamos construyendo el codigo a partir de debbing 
#Ej: def suma - Escribimos los test de como se deberia comportar y luego es que definimos la funcion 

 #unit testing - prubeas unitarias 

import unittest

#Este es el paso 2 
def suma(num_1, num_2):
    return abs(num_1 + num_2)

#Este es el paso 1 
class cajaNegraText(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10 
        num_2 = 5

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 15)
    
    def test_suma_dos_negativos(self):
        num_1 = -10 
        num_2 = -7

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -17)

if __name__ == "__main__":
    unittest.main()

#Integration testing - Pruebas integrales