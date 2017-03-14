import unittest # El modulo unittest crea un objeto de la clase que tiene por parametro unittest.TestCase corre primero la funcion setUp y luego las que empiezan por test

from rectangle import Rectangle
from rectangle import overlap

class RectangleTestCase(unittest.TestCase): # Esta clase hace la prueba, debe tener el unittest.TestCase de parametro
    def setUp(self): # Esta funcion crea unos objetos
        self.rec = Rectangle()
        self.rec_b = Rectangle()
    
    def test_default_size(self): # Una funcion que comienza por test la corre como un test
        self.assertEqual(self.rec.size(),(10,10),
                         'tamano de inicio incorrecto')

    def test_resize(self):
        self.rec.resize(100,150)
        self.assertEqual(self.rec.size(),(100,150),'mal tamano despues de resize')

    def test_overlap_symmetry(self):
        self.rec.recenter(20.0,20.0)
        self.assertEqual(overlap(self.rec,self.rec_b),overlap(self.rec_b,self.rec), 'mala simetria en overlap')

    def test_overlap(self):
        self.rec.recenter(0,0)
        self.rec.resize(2,2)
        self.rec_b.recenter(0,0)
        self.rec_b.resize(1,1)
        
        self.assertEqual(overlap(self.rec,self.rec_b),True,'se deberian solapar')
