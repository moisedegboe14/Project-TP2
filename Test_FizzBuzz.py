import unittest
from FizzBuzz import *

class Test_FizzBuzz (unittest.TestCase):
    def setUp(self):
        self.instance = FizzBuzz()


    def test_affiche_sans_parametre(self):
        self.assertEqual(self.instance.affiche(),"12")

if __name__ == '__main__':
    unittest.main()