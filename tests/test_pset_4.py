import unittest
from psets import pset_4

class TestPset4(unittest.TestCase):
    def test_bmi_information(self):
        self.assertEqual(pset_4.bmi_information(50, 170), "Your BMI is 17.3 and your category is nutritional deficiency.", 'Should be "Your BMI is 17.3 and your category is nutritional deficiency."')
        self.assertEqual(pset_4.bmi_information(70, 190), "Your BMI is 19.4 and your category is low risk.", 'Should be "Your BMI is 19.4 and your category is low risk."')
        self.assertEqual(pset_4.bmi_information(70, 167), "Your BMI is 25.1 and your category is moderate risk.", 'Should be "Your BMI is 25.1 and your category is moderate risk."')
        self.assertEqual(pset_4.bmi_information(90, 180), "Your BMI is 27.8 and your category is high risk.", 'Should be "Your BMI is 27.8 and your category is high risk."')

    def test_reverse(self):
        self.assertEqual(pset_4.reverse("hello"), "olleh", "Should be olleh")
        self.assertEqual(pset_4.reverse("aloha"), "ahola", "Should be ahola")
        self.assertEqual(pset_4.reverse("Ronaldo7"), "7odlanoR", "Should be 7odlanoR")
    
    def test_palindrome(self):
        self.assertFalse(pset_4.is_palindrome("hello"), "Should be False as not equal")
        self.assertFalse(pset_4.is_palindrome("Triple H"), "Should be False as not equal")
        self.assertTrue(pset_4.is_palindrome("racecar"), "Should be True as equal")
        self.assertTrue(pset_4.is_palindrome("kayak"), "Should be False as equal")

if __name__ == '__main__':
    unittest.main()