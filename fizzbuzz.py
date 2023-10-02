import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):

    def test_affiche_sans_parameter(self):
        result = affiche()
        self.assertEqual(result, "")

    def test_affiche_avec_parameter(self):
        self.assertEqual(affiche(15), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")

    def test_affiche_avec_range(self):
        self.assertEqual(affiche(5, 10), "BuzzFizz78FizzBuzz")

if __name__ == '__main__':
    unittest.main()