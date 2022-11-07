import unittest
from psets import pset_3A

class TestPset3A(unittest.TestCase):
    def test_calculate_sum_odd(self): 
        self.assertEqual(pset_3A.calculate_sum_odd(0), 0, "Should be 0")
        self.assertEqual(pset_3A.calculate_sum_odd(-1), 0, "Should be 0")
        self.assertEqual(pset_3A.calculate_sum_odd(5), 4, "Should be 4")
        self.assertEqual(pset_3A.calculate_sum_odd(6), 9, "Should be 9")

    def test_alternating(self): 
        self.assertEqual(pset_3A.alternating(0), 0, "Should be 0")
        self.assertEqual(pset_3A.alternating(1), 1, "Should be 1")
        self.assertEqual(pset_3A.alternating(2), 0.5, "Should be 0.5")
        self.assertEqual(pset_3A.alternating(4), 0.5833333333333333, "Should be 0.5833333333333333")

    def test_compound_interest(self):
        self.assertEqual(pset_3A.compound_interest(100, 0.05, 6), 102.53, "Should be 102.53")    
        self.assertEqual(pset_3A.compound_interest(100, 0.05, 0), 100, "Should be 100")    
        self.assertEqual(pset_3A.compound_interest(100, 0.60, 12), 179.59, "Should be 179.59") 

    def test_regular_savings(self):
        self.assertEqual(pset_3A.regular_savings(100, 0.05, 6), 608.81, "Should be 608.81")    

    def test_sum_of_series(self):
        self.assertEqual(pset_3A.sum_of_series(0), 0, "Should be 0")    
        self.assertEqual(pset_3A.sum_of_series(1), 1, "Should be 1")    
        self.assertEqual(pset_3A.sum_of_series(10), 1.5497677311665408, "Should be 1.5497677311665408")    

    def test_fraction_of_pisq(self):    
        self.assertEqual(pset_3A.fraction_of_pisq(1.5), 0.91189065278104, "Should be 0.91189065278104")

    def test_terms_required(self):
        self.assertEqual(pset_3A.terms_required(0.9), 6, "Should be 6")

    def test_is_prime(self):
        self.assertTrue(pset_3A.is_prime(23), "Should be True")
        self.assertTrue(pset_3A.is_prime(19), "Should be True")
        self.assertFalse(pset_3A.is_prime(8), "Should be False")
        self.assertFalse(pset_3A.is_prime(32), "Should be False")

    def test_calculate_sum_even(self): 
        self.assertEqual(pset_3A.calculate_sum_even(0), 0, "Should be 0")
        self.assertEqual(pset_3A.calculate_sum_even(6), 6, "Should be 6")
        self.assertEqual(pset_3A.calculate_sum_even(7), 12, "Should be 12")
        self.assertEqual(pset_3A.calculate_sum_even(8), 12, "Should be 12")

    def test_alternating_while(self): 
        self.assertEqual(pset_3A.alternating_while(0.249), 0.5833333333333333, "Should be 0.5833333333333333")
        self.assertEqual(pset_3A.alternating_while(0.199), 0.7833333333333332, "Should be 0.7833333333333332")

if __name__ == '__main__':
    unittest.main()
