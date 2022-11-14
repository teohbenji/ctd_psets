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