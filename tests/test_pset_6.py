import unittest
from psets import pset_6

class TestPset6(unittest.TestCase):
    def test_get_average_sublist(self):
        self.assertEqual(pset_6.get_average_sublist([[1, 2], [3, 2, 5], [20, 1, 3]], 0), 1.5, "Average is 1.5")
        self.assertEqual(pset_6.get_average_sublist([[1, 2], [3, 2, 5], [20, 1, 3]], 1), 3.3, "Average is 3,3")
        self.assertEqual(pset_6.get_average_sublist([[1, 2], [3, 2, 5], [20, 1, 3]], -1), 8, "Average is 8")
        self.assertIsNone(pset_6.get_average_sublist([[1, 2], [3, 2, 5], [20, 1, 3]], 3), "n out of range, None")

    def test_has_list(self):
        self.assertTrue(pset_6.has_list([1, [1, 2], "dog"]), "True. Contains list [1, 2]")
        self.assertTrue(pset_6.has_list([[1, 2], 2, "dog"]), "True. Contains list [1, 2]")
        self.assertFalse(pset_6.has_list([1, 2, "dog"]), "False. No list.")
        self.assertFalse(pset_6.has_list([1, 2, 3]), "False. No list.")

    def test_max_list(self):
        self.assertEqual(pset_6.max_list([100, 1, 2]), [100], "Should be [100]")
        self.assertEqual(pset_6.max_list([[1, 10, 2], [8, 7], [3, 4, 2, 1]]), [10, 8, 4], "Should be [10, 8, 4]")
        self.assertEqual(pset_6.max_list([[1, 2, 3], [8, 7], [9, 4, 2, 1]]), [3, 8, 9], "Should be [3, 8, 9]")

    def test_find_average_of_lists(self):
        self.assertEqual(pset_6.find_average_of_lists([[1, 2], [3, 2, 5], [20, 1, 3]]), ([1.5, 3.33, 8], 4.62), "Rounded averages: [1.5, 3.33, 8], Average is 4.62 (rounded down from 4.625)")    
        self.assertEqual(pset_6.find_average_of_lists([[6, 5], [3, 2, 6], [0, 1, 2]]), ([5.5, 3.67, 1], 3.12), "Rounded averages: [5.5, 3.67, 1], Average is 3.12 (rounded down from 3.125)")    
        self.assertEqual(pset_6.find_average_of_lists([-6, 5]), ([-0.5], -0.5), "Rounded averages: [-5.5], Average is -5.5")    