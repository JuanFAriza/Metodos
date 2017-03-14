import unittest # UnitTest es la libreria encargada de los tests, lo corro como python -m unittest nombrearchivo(sin .py)

def fun(x):
    return x+1

class MyTest(unittest.TestCase): # Debo crear una clase en la que se pase 
    def test(self): # Una funcion que comience por test la ejecuta como un test
        self.assertEqual(fun(4),4) # Debo saber que resultado estoy buscando
