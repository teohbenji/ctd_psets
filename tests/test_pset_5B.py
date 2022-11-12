import unittest
from psets import pset_5B

class TestPset5A(unittest.TestCase):
    def test_create_dictionary(self):
        self.assertEqual(pset_5B.increase_value({1: 10, 2: 20}, 1), {1: 11, 2: 20}, "kv pair 1:10 is now 1:11")
        self.assertEqual(pset_5B.increase_value({1: 10, 2: 20}, 2), {1: 10, 2: 21}, "kv pair 2:20 is now 2:21")
        self.assertEqual(pset_5B.increase_value({1: 10, 2: 20}, 3), {1: 10, 2: 20}, "kv pairs unchanged")

    def test_translate_point(self):
        self.assertEqual(pset_5B.translate_point({'A': (0, 0), 'B': (1, -1), 'C': (2, -2)}, 'D', (1, 1)), {'A': (0, 0), 'B': (1, -1), 'C': (2, -2)}, "Same dict as key doesn't exist in dd")
        self.assertEqual(pset_5B.translate_point({'A': (0, 0), 'B': (1, -1), 'C': (2, -2)}, 'A', (3, 1)), {'A': (3, 1),  'B': (1, -1), 'C': (2, -2)}, "Vector A translated to (3, 1)")
        self.assertEqual(pset_5B.translate_point({'A': (0, 0), 'B': (1, -1), 'C': (2, -2)}, 'B', (-1, 2)), {'A': (0, 0),  'B': (0, 1), 'C': (2, -2)}, "Vector B translated to (0, 1)")
        self.assertEqual(pset_5B.translate_point({'A': (0, 0), 'B': (1, -1), 'C': (2, -2)}, 'C', (1.5, -4.5)), {'A': (0, 0),  'B': (1, -1), 'C': (3.5, -6.5)}, "Vector C translated to (0, 1)")

    def test_translate_point_new(self):
        self.assertEqual(pset_5B.translate_point_new({'A': (0, 0), 'B': (1, -1), 'C': (2, -2)}, 'D', (1, 1)), {'A': (0, 0), 'B': (1, -1), 'C': (2, -2)}, "Same dict as key doesn't exist in dd")
        self.assertEqual(pset_5B.translate_point_new({'A': (0, 0), 'B': (1, -1), 'C': (2, -2)}, 'A', (3, 1)), {'A': (3, 1),  'B': (1, -1), 'C': (2, -2)}, "Vector A translated to (3, 1)")
        self.assertEqual(pset_5B.translate_point_new({'A': (0, 0), 'B': (1, -1), 'C': (2, -2)}, 'B', (-1, 2)), {'A': (0, 0),  'B': (0, 1), 'C': (2, -2)}, "Vector B translated to (0, 1)")
        self.assertEqual(pset_5B.translate_point_new({'A': (0, 0), 'B': (1, -1), 'C': (2, -2)}, 'C', (1.5, -4.5)), {'A': (0, 0),  'B': (1, -1), 'C': (3.5, -6.5)}, "Vector C translated to (0, 1)")

    def test_replace_values(self):
        self.assertEqual(pset_5B.replace_values([1, 3, 2, 1, 4, 2, 1, 1, 3, 4], 5, 0), [1, 3, 2, 1, 4, 2, 1, 1, 3, 4], "Same dict as key doesn't exist")
        self.assertEqual(pset_5B.replace_values([1, 3, 2, 1, 4, 2, 1, 1, 3, 4], 1, 0), [0, 3, 2, 0, 4, 2, 0, 0, 3, 4], "Every 1 replaced by 0")
        self.assertEqual(pset_5B.replace_values([1, 3, 2, 1, 4, 2, 1, 1, 3, 4], 2, 0), [1, 3, 0, 1, 4, 0, 1, 1, 3, 4], "Every 2 replaced by 0")
        self.assertEqual(pset_5B.replace_values([1, 3, 2, 1, 4, 2, 1, 1, 3, 4], 3, 0), [1, 0, 2, 1, 4, 2, 1, 1, 0, 4], "Every 3 replaced by 0")
        self.assertEqual(pset_5B.replace_values([1, 3, 2, 1, 4, 2, 1, 1, 3, 4], 4, 0), [1, 3, 2, 1, 0, 2, 1, 1, 3, 0], "Every 4 replaced by 0")

    def test_replace_values_new(self):
        self.assertEqual(pset_5B.replace_values_new([1, 3, 2, 1, 4, 2, 1, 1, 3, 4], 5, 0), [1, 3, 2, 1, 4, 2, 1, 1, 3, 4], "Same dict as key doesn't exist")
        self.assertEqual(pset_5B.replace_values_new([1, 3, 2, 1, 4, 2, 1, 1, 3, 4], 1, 0), [0, 3, 2, 0, 4, 2, 0, 0, 3, 4], "Every 1 replaced by 0")
        self.assertEqual(pset_5B.replace_values_new([1, 3, 2, 1, 4, 2, 1, 1, 3, 4], 2, 0), [1, 3, 0, 1, 4, 0, 1, 1, 3, 4], "Every 2 replaced by 0")
        self.assertEqual(pset_5B.replace_values_new([1, 3, 2, 1, 4, 2, 1, 1, 3, 4], 3, 0), [1, 0, 2, 1, 4, 2, 1, 1, 0, 4], "Every 3 replaced by 0")
        self.assertEqual(pset_5B.replace_values_new([1, 3, 2, 1, 4, 2, 1, 1, 3, 4], 4, 0), [1, 3, 2, 1, 0, 2, 1, 1, 3, 0], "Every 4 replaced by 0")

    def test_equation_of_line(self):
        self.assertEqual(pset_5B.equation_of_line((5, 4), (-5, -6)), (-10, 10, -10), "Factorised eqn of line: y - x + 1 = 0 after factorising out -10")
        self.assertEqual(pset_5B.equation_of_line((5, -10), (-5, 5)), (-10, -15, -25), "Factorised eqn of line: 2y + 3x + 5 = 0 after factorising out -5")
        self.assertEqual(pset_5B.equation_of_line((18, -5), (-5, 0.75)), (-23, -5.75, -11.5), "Factorised eqn of line: 4y + x + 2 = 0 after factorising out -5.75")
    
    def test_reflect(self):
        self.assertEqual(pset_5B.reflect((-3, 4), (2, 0, -4)), (-3, 0), "Reflected point is (-3, 0)")
        self.assertEqual(pset_5B.reflect((-3, 4), (1, 0, 0)), (-3, -4), "Reflected point about x-axis is (-3, -4)")
        self.assertEqual(pset_5B.reflect((-3, 4), (0, 1, 0)), (3, 4), "Reflected point about y-axis is (3, 4)")
        self.assertEqual(pset_5B.reflect((-4, 3), (1, -1, 0)), (3, -4), "Reflected point about origin is (3, -4)")

    def test_reflect_triangle(self):
        self.assertEqual(pset_5B.reflect_triangle({'A': (1, 2), 'B': (-3, 4), 'C': (-1, 2)}, 'B'), {'A': (1, 2), 'B': (-3, 0), 'C': (-1, 2)}, "New value of B is (-3, 0)")
        self.assertEqual(pset_5B.reflect_triangle({'A': (1, 1), 'B': (5, 4), 'C': (-5, -6)}, 'A'), {'A': (2, 0), 'B': (5, 4), 'C': (-5, -6)}, "New value of A is (2, 0)")

if __name__ == '__main__':
    unittest.main()