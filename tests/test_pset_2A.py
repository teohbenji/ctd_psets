# https://www.youtube.com/watch?v=6tNS--WetLI
import unittest
from psets import pset_2A

#class that inherits from unittest.TestCase

class TestPset2A(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertEqual(pset_2A.calculate_bmi(85.12,185.55), 24.7, "Should be 24.7")
        self.assertEqual(pset_2A.calculate_bmi(147.34,216.688), 31.4, "Should be 31.4")
        self.assertEqual(pset_2A.calculate_bmi(67.56,169.1), 23.6, "Should be 23.6")

    def test_position_velocity(self):
        self.assertEqual(pset_2A.position_velocity(5.0, 0), (0.0, 5.0), "Should be (0.0, 5.0)")
        self.assertEqual(pset_2A.position_velocity(10.0, 1), (5.095, 0.19), "Should be (5.095, 0.19)")
        self.assertEqual(pset_2A.position_velocity(5.886, 0.3), (1.324, 2.943), "Should be (1.324, 2.943)")

    def test_decay(self): 
        self.assertEqual(pset_2A.decay(2, 0), 1.0, "Should be 1.0")
        self.assertEqual(pset_2A.decay(2, 0.5), 0.19876611034641298, "Should be 0.19876611034641298")

    def test_describe_bmi(self): 
        self.assertEqual(pset_2A.describe_bmi(18), "nutritional deficiency", 'Should be "nutritional deficiency"')
        self.assertEqual(pset_2A.describe_bmi(18.5), "low risk", 'Should be "low risk"')
        self.assertEqual(pset_2A.describe_bmi(23), "moderate risk", 'Should be "moderate risk"')
        self.assertEqual(pset_2A.describe_bmi(27.5), "high risk", 'Should be "high risk"')

    def test_describe_bmi(self): 
        self.assertFalse(pset_2A.is_positive_even(-1), "Should be False")
        self.assertTrue(pset_2A.is_positive_even(32), "Should be True")
        self.assertFalse(pset_2A.is_positive_even(1), "Should be False")

    def test_letter_grade(self): 
        self.assertEqual(pset_2A.letter_grade(90), "A", "Should be A")
        self.assertEqual(pset_2A.letter_grade(80), "B", "Should be B")
        self.assertEqual(pset_2A.letter_grade(70), "C", "Should be C")
        self.assertEqual(pset_2A.letter_grade(60), "D", "Should be D")
        self.assertEqual(pset_2A.letter_grade(59), "E", "Should be E")
        self.assertIsNone(pset_2A.letter_grade(420), "Should be None")
        self.assertIsNone(pset_2A.letter_grade(-21), "Should be None")


    def test_largest_area(self):
        self.assertIsNone(pset_2A.largest_area(-1, 2, 3), "Should be None")
        self.assertIsNone(pset_2A.largest_area(1, -2, 3), "Should be None")
        self.assertIsNone(pset_2A.largest_area(1, 2, -3), "Should be None")
        self.assertIsNone(pset_2A.largest_area(1, 2, 3), "Should be None")
        self.assertEqual(pset_2A.largest_area(10, 3, 4), 42, "Should be 42")
        self.assertEqual(pset_2A.largest_area(10, 3, 2), 56, "Should be 56")
        self.assertEqual(pset_2A.largest_area(10, 2, 6), 48, "Should be 48")
        self.assertEqual(pset_2A.largest_area(0, 0, 0), 0, "Should be 0")
        self.assertEqual(pset_2A.largest_area(10, 0, 0), 100, "Should be 100")

if __name__ == '__main__':
    unittest.main()