import unittest
from psets import pset_2C

class TestPset2C(unittest.TestCase):
    def test_sequence(self): 
        self.assertIsNone(pset_2C.sequence(-0.6), "Should be None")
        self.assertIsNone(pset_2C.sequence(-3), "Should be None")
        self.assertEqual(pset_2C.sequence(5), 1.1726, "Should be 1.1726")
        self.assertEqual(pset_2C.sequence(9), 1.2583, "Should be 1.2583")

    def test_check_value(self):
        self.assertFalse(pset_2C.check_value(7, 5, 8, 6), "Should be False") #x smaller than n1
        self.assertFalse(pset_2C.check_value(5, 7, 8, 6), "Should be False") #x smaller than n2
        self.assertFalse(pset_2C.check_value(5, 5, 5, 6), "Should be False") #x greater than n2
        self.assertFalse(pset_2C.check_value(5, 5, 5, 5), "Should be False") #x equals everything
        self.assertTrue(pset_2C.check_value(2, 1, 7, 6), "Should be True") #x equals everything
        self.assertTrue(pset_2C.check_value(-2, -1, 1, 0), "Should be True") #x equals everything

if __name__ == '__main__':
    unittest.main()