import unittest
from code_binaire import Bit, CodeBinaire, AuMoinsUnBitErreur

class TestCodeBinaire(unittest.TestCase):
    
    def test_egalite(self):
        c1 = CodeBinaire(Bit.BIT_0)
        c2 = CodeBinaire(Bit.BIT_0)
        c3 = CodeBinaire(Bit.BIT_1)
        self.assertEqual(c1, c2)
        self.assertNotEqual(c1, c3)
        
        c4 = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
        c5 = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
        c6 = CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)
        self.assertEqual(c4, c5)
        self.assertNotEqual(c4, c6)
    
    def test_ajouter(self):
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
        c.ajouter(Bit.BIT_0)
        expected = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
        self.assertEqual(c, expected)
    
    def test_getitem(self):
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
        
        self.assertEqual(c[0], Bit.BIT_0)
        self.assertEqual(c[1], Bit.BIT_1)
        self.assertEqual(c[2], Bit.BIT_0)
        
        sub = c[1:3]
        expected = CodeBinaire(Bit.BIT_1, Bit.BIT_0)
        self.assertEqual(sub, expected)
    
    def test_setitem(self):
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
        
        c[1] = Bit.BIT_0
        expected = CodeBinaire(Bit.BIT_0, Bit.BIT_0, Bit.BIT_0)
        self.assertEqual(c, expected)
        
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
        c[0:2] = [Bit.BIT_1, Bit.BIT_1, Bit.BIT_0]
        expected = CodeBinaire(Bit.BIT_1, Bit.BIT_1, Bit.BIT_0, Bit.BIT_0)
        self.assertEqual(c, expected)
        
        c = CodeBinaire(Bit.BIT_1, Bit.BIT_1, Bit.BIT_0, Bit.BIT_0)
        c[0:2] = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
        expected = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0, Bit.BIT_0)
        self.assertEqual(c, expected)
        
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
        c[0:2] = [Bit.BIT_1, Bit.BIT_1, Bit.BIT_0]
        expected = CodeBinaire(Bit.BIT_1, Bit.BIT_1, Bit.BIT_0)
        self.assertEqual(c, expected)
        
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
        c[0:3] = [Bit.BIT_1]
        expected = CodeBinaire(Bit.BIT_1)
        self.assertEqual(c, expected)
    
    def test_delitem(self):
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
        
        del c[1]
        expected = CodeBinaire(Bit.BIT_0, Bit.BIT_0)
        self.assertEqual(c, expected)
        
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)
        del c[1:3]
        expected = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
        self.assertEqual(c, expected)
    
    def test_add(self):
        c1 = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
        c2 = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
        result = c1 + c2
        expected = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)
        self.assertEqual(result, expected)
        
        with self.assertRaises(TypeError):
            c1 + "not a code"
    
    def test_len(self):
        c = CodeBinaire(Bit.BIT_0)
        self.assertEqual(len(c), 1)
        
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
        self.assertEqual(len(c), 3)
        
        c.ajouter(Bit.BIT_1)
        self.assertEqual(len(c), 4)
        
        c2 = CodeBinaire(Bit.BIT_1)
        c3 = c + c2
        self.assertEqual(len(c3), 5)
    
    def test_au_moins_un_bit_erreur(self):
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
        with self.assertRaises(AuMoinsUnBitErreur):
            del c[0]
            del c[0]
        
        c = CodeBinaire(Bit.BIT_0)
        with self.assertRaises(AuMoinsUnBitErreur):
            del c[:]
        
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
        with self.assertRaises(AuMoinsUnBitErreur):
            c[0:2] = []
    
    def test_repr(self):
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
        repr_str = repr(c)
        self.assertEqual(repr_str, "CodeBinaire(Bit.BIT_0, Bit.BIT_1)")
        c2 = eval(repr_str)
        self.assertEqual(c, c2)
    
    def test_str(self):
        c = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
        self.assertEqual(str(c), "010")
        
        self.assertEqual(str(Bit.BIT_0), "0")
        self.assertEqual(str(Bit.BIT_1), "1")

if __name__ == '__main__':
    unittest.main()