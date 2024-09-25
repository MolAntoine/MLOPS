import unittest
from mlopsantoinem.main import donne_des_sous, compte_en_banque

class MyTestCase(unittest.TestCase):
    def test_donne_des_sous(self):
        compte_en_banque = donne_des_sous(8,10)
        self.assertEqual(18, compte_en_banque) # add assertion here

    def test_dds2(self):
        test = donne_des_sous(12,10)
        self.assertEqual(24, test)

if __name__ == '__main__':
    unittest.main()
