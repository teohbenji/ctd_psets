import unittest
from psets import pset_2B

class TestPset2B(unittest.TestCase):
    def test_compound_interest(self):
        self.assertEqual(pset_2B.compound_interest(1, 0.03, 1, 1), 1.03, "Should be 1.03")
        self.assertEqual(pset_2B.compound_interest(1, 0.12, 12, 1), 1.127, "Should be 1.127")
        self.assertEqual(pset_2B.compound_interest(1, 1, 1000, 1), 2.717, "Should be 2.717")

    def test_area_vol_cylinder(self):
        self.assertEqual(pset_2B.area_vol_cylinder(3.5, 1), (38.48, 38.48), "Should be 38.48, 38.48")
        self.assertEqual(pset_2B.area_vol_cylinder(3.1415, 4.2), (31.00, 130.20), "Should be 31.00, 130.20")
        self.assertEqual(pset_2B.area_vol_cylinder(10, 0.5), (314.16, 157.08), "Should be 314.16, 157.08")

    def test_seconds_to_hours(self):
        self.assertEqual(pset_2B.seconds_to_hours(29500), (8, 11, 40), "Should be (8, 11, 40)")
        self.assertEqual(pset_2B.seconds_to_hours(7210), (2, 0, 10), "Should be (2, 0, 10)")
        self.assertEqual(pset_2B.seconds_to_hours(3000), (0, 50, 0), "Should be (0, 50, 0)")

    def test_fahrenheit_to_celsius(self):
        self.assertIsNone(pset_2B.fahrenheit_to_celsius(-475), "Should be None")
        self.assertEqual(pset_2B.fahrenheit_to_celsius(52), 11.11 , "Should be 52")
        self.assertEqual(pset_2B.fahrenheit_to_celsius(77), 25, "Should be 77")


if __name__ == '__main__':
    unittest.main()