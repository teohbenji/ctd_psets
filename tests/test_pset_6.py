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

    def test_get_zero_matrix(self):
        self.assertEqual(pset_6.get_zero_matrix(1, 2), [[0, 0]], "1x2 zero matrix created")
        self.assertEqual(pset_6.get_zero_matrix(2, 2), [[0, 0], [0, 0]], "2x2 zero matrix created")
        self.assertEqual(pset_6.get_zero_matrix(3, 3), [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "2x2 zero matrix created")

    def test_transpose_matrix(self):
        self.assertEqual(pset_6.transpose_matrix([[1, 2], [3, 4]]), [[1, 3], [2, 4]], "Transposed is [[1, 3], [2, 4]]")
        self.assertEqual(pset_6.transpose_matrix([[1], [3]]), [[1, 3]], "Transposed is [[1, 3], [2, 4]]")
        self.assertEqual(pset_6.transpose_matrix([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]], "Transposed is [[1, 4], [2, 5], [3, 6]]")
    
    def test_process_scores(self):
        with open('files/test_scores.txt') as f:
            self.assertEqual(pset_6.process_scores(f), (21, 3.5), "Sum is 21. Average is 21/6 = 3.5")
            f.close()
    
    def test_read_fdi(self):
        comparison_dict = {'1998': 2995.4, '1999': 15443.7, '2000': 22174.1, '2001': 18314.6, '2002': 24611.3, '2003': 30256.9, '2004': 43943.7, '2005': 53896.3}
        with open('files/fdi.csv') as f:
            self.assertEqual(pset_6.read_fdi(f), comparison_dict, "Different from comparison dict")
            
    def test_gc_content(self):
        with open('files/test_dna.txt') as f:
            self.assertEqual(pset_6.gc_content(f), 18.5, "Percentage should be (5/27) * 100% = 18.5%")

    def test_scalar_multiply(self):
        original_matrix = [[2, 4], [6, 8], [10, 12]]

        self.assertEqual(pset_6.scalar_multiply(original_matrix, 0.5), [[1, 2], [3, 4], [5, 6]], "Should be [[1, 2], [3, 4], [5, 6]]")
        self.assertTrue(pset_6.scalar_multiply(original_matrix, 0.5) is original_matrix, "Original matrix is modified")
    
    def test_scalar_multiply_new(self):
        original_matrix = [[4, 8], [12, 16]]

        self.assertEqual(pset_6.scalar_multiply_new(original_matrix, 0.5), [[2, 4], [6, 8]], "Should be [[2, 4], [6, 8]]")
        self.assertFalse(pset_6.scalar_multiply_new(original_matrix, 0.5) is original_matrix, "Original matrix is not modified")