import unittest
from psets import pset_3B

class TestPset3B(unittest.TestCase):
    def test_median(self):
        self.assertEqual(pset_3B.median([1, 2, 3, 4, 5, 6, 7]), 4, "Should be 4")
        self.assertEqual(pset_3B.median([1, 2, 3, 4, 5, 6]), 3.5, "Should be 3.5")
        self.assertEqual(pset_3B.median([2, 4, 6]), 4, "Should be 4") 
        self.assertEqual(pset_3B.median([2, 4, 6, 8]), 5, "Should be 5")

    def test_middle_list(self):
        self.assertEqual(pset_3B.middle_list([1, 2, 3, 4, 5, 6, 7]), [2, 3, 4, 5, 6], "Should be [2,3,4,5,6]")
        self.assertEqual(pset_3B.middle_list([1, 2, 3, 4, 5, 6]), [2 , 3, 4, 5], "Should be [2,3,4,5]")
        self.assertEqual(pset_3B.middle_list([2, 4, 6]), [4], "Should be [2,4,6]")

    def test_swap_elements(self):
        self.assertIsNone(pset_3B.swap_elements([1, 2, 3], 3, 1), "Should be None, as index1 is out of range")   
        self.assertIsNone(pset_3B.swap_elements([1, 2, 3], -4, 1), "Should be None, as index2 is out of range")   
        self.assertEqual(pset_3B.swap_elements([5, 6, 7, 8], 1, 2), [5, 7, 6, 8], "Should be [5,7,6,8]")   
        self.assertEqual(pset_3B.swap_elements([5, 6, 7, 8], 1, 1), [5, 6, 7, 8], "Should be [5,6,7,8]")   
        self.assertEqual(pset_3B.swap_elements([5, 6, 7, 8], -4, 3), [8, 6, 7, 5], "Should be [8,6,7,5]")   

    def test_sum_odd_numbers(self): 
        self.assertEqual(pset_3B.sum_odd_numbers([1, 2, 3, 4, 5]), 9, "Should be 9")
        self.assertEqual(pset_3B.sum_odd_numbers([2, 4, 6, 8, 10]), 0, "Should be 0")
        self.assertEqual(pset_3B.sum_odd_numbers([2, 4, 6, 8, 11]), 11, "Should be 11")

    def test_hailstone(self):
        self.assertEqual(pset_3B.hailstone(20), [20, 10, 5, 16, 8, 4, 2, 1], "Should be [20, 10, 5, 16, 8, 4, 2, 1]")
        self.assertEqual(pset_3B.hailstone(3), [3, 10, 5, 16, 8, 4, 2, 1], "Should be [3, 10, 5, 16, 8, 4, 2, 1]")

    def test_get_odd_numbers(self):
        self.assertEqual(pset_3B.get_odd_numbers([1, 3, 5]), [1, 3, 5], "Should be [1,3,5]")
        self.assertEqual(pset_3B.get_odd_numbers([2, 4, 6]), [], "Should be [], no odd numbers")
        self.assertEqual(pset_3B.get_odd_numbers([1, 2, 5]), [1, 5], "Should be [2]")

    #TODO: write 1 more test case
    def test_moving_average(self):
        self.assertEqual(pset_3B.moving_average([30.0, 20.0, 40.0, 50.0, 25.0, 70.0]), [30.0, 36.7, 38.3, 48.3], "Should be [30.0, 36.7, 38.3, 48.3]")

    def test_trapezoidal_rule(self):
        self.assertEqual(pset_3B.trapezoidal_rule([3, 7, 11, 9, 3], 2), 60, "Should be 60")
        self.assertEqual(pset_3B.trapezoidal_rule([1, 2, 3, 4, 5], 6), 72, "Should be 72")

    #TODO: write 1 more test case
    def test_left_riemann_sum(self):
        self.assertEqual(pset_3B.left_riemann_sum([0, 2, 3, 5, 6], [1, 1.5, 1.7, 1.9, 2.0]), 8.8, "Should be 8.8")

if __name__ == '__main__':
    unittest.main()