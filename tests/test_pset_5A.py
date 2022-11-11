import unittest
from psets import pset_5A

class TestPset5A(unittest.TestCase):
    def test_create_dictionary(self):
        self.assertIsNone(pset_5A.create_dictionary(['apple'],[0, 2]), "None as list lengths aren't equal")
        self.assertEqual(pset_5A.create_dictionary(['apple', 'orange'],[1.0, 2.5]), {'apple':1.0, 'orange':2.5}, "Should be {'apple':1.0, 'orange':2.5}")
        self.assertEqual(pset_5A.create_dictionary(['apple', 'orange', 'banana'],[1.0, 2.5, 3.6]), {'apple':1.0, 'orange':2.5, 'banana':3.6}, "Should be {'apple':1.0, 'orange':2.5, 'banana':3.6}")

    def test_get_value(self):
        self.assertIsNone(pset_5A.get_value({"apple": 1}, "banana"), '"banana" is not a key in dd')
        self.assertEqual(pset_5A.get_value({"apple": 1}, "apple"), 1, 'Should be 1')

    def test_extract_data(self):
        self.assertIsNone(pset_5A.extract_data({'A': (0, 1)}, "B"), "'B' is not a key in dd")
        self.assertEqual(pset_5A.extract_data({'A': (4, 5), 'B': (2, -1.5), 'C':(-3, 0.9)}, "A"), 6.40, "Should be")
        self.assertEqual(pset_5A.extract_data({'A': (4, 5), 'B': (2, -1.5), 'C':(-3, 0.9)}, "B"), 2.5, "Should be")
        self.assertEqual(pset_5A.extract_data({'A': (4, 5), 'B': (2, -1.5), 'C':(-3, 0.9)}, "C"), 3.13, "Should be")

    def test_get_base_counts(self):
        self.assertEqual(pset_5A.get_base_counts("AAACCCG"), {"A": 3, "C": 3, "G": 1, "T": 0}, "Should be {'A': 3, 'C': 3, 'G': 1, 'T': 0}")
        self.assertEqual(pset_5A.get_base_counts("ACCCCCGGGGGTT"), {"A": 1, "C": 5, "G": 5, "T": 2}, "Should be {'A': 3, 'C': 3, 'G': 1, 'T': 0}")
        self.assertEqual(pset_5A.get_base_counts("AAACCCt"), "The input DNA string is invalid", "Invalid string due to invalid character")
    
    def test_evaluate_polynomial(self):
        self.assertEqual(pset_5A.evaluate_polynomial({3: 1, 2: 1, 1: 1, 0: 1}, 2), 15, "Should be 15") 
        self.assertEqual(pset_5A.evaluate_polynomial({3: 2, 2: 2, 1: 2, 0: 2}, 1.5), 16.25, "Should be 16.25") 
        self.assertEqual(pset_5A.evaluate_polynomial({3: 3, 2: 2, 1: 1, 0: 0}, 2.25), 46.55, "Should be 16.25") 

    def test_diff(self):
        self.assertEqual(pset_5A.diff({0: -3, 3: 2, 5:  -1}), {2: 6, 4: -5}, "Derivative should be -5x^4 + 6x^2")
        self.assertEqual(pset_5A.diff({2: 3, 1: 2, 0: 1}), {1: 6, 0: 2}, "Derivative should be 6x + 2")
        self.assertEqual(pset_5A.diff({-3: -2, -2: -1, -1: 3}), {-4: 6, -3: 2, -2: -3}, "Derivative should be 6x^-4 + 2x^-3 - 3x^-2")


if __name__ == '__main__':
    unittest.main()