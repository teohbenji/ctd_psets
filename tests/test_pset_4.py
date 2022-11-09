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

    def test_match(self):
        self.assertFalse(pset_4.match("mob", "mobile"), "mob and ile dont match")
        self.assertFalse(pset_4.match("occe", "soccer"), "occe and ccer dont match")
        self.assertTrue(pset_4.match("bile", "mobile"), "Should be True as equal")
        self.assertTrue(pset_4.match("ccer", "soccer"), "Should be True as equal")

    def test_clean_string(self):
        self.assertEqual(pset_4.clean_string("It's over Anakin, I have the high ground."), "Its over Anakin I have the high ground", 'Should be "Its over Anakin I have the high ground"')
        self.assertEqual(pset_4.clean_string("Ankara Messi, ankara Messi, ankara Messi!"), "Ankara Messi ankara Messi ankara Messi", 'Should be "Ankara Messi ankara Messi ankara Messi"')

    def test_digits_in_string(self):
        self.assertEqual(pset_4.digits_in_string("Hello"), 0, "String has 0 digits")
        self.assertEqual(pset_4.digits_in_string("a1b2c3"), 3, "String has 3 digits")
        self.assertEqual(pset_4.digits_in_string("2134132"), 7, "String has 7 digits")

    def test_check_password(self):
        self.assertFalse(pset_4.check_password("Hello"), "False because pwd contains less than 8 characters")
        self.assertFalse(pset_4.check_password("1943h32%!"), "False because pwd contains non-alphanumeric characters")
        self.assertFalse(pset_4.check_password("oqfjojw1"), "False because pwd doesn't contain 2 or more digits")
        self.assertTrue(pset_4.check_password("I1aslf1980ad"), "Valid because pwd meets all requirements")

    def test_longest_common_prefix(self):
        self.assertEqual(pset_4.longest_common_prefix("Man", "Manga"), "Man", "Man is the common prefix")
        self.assertEqual(pset_4.longest_common_prefix("Sing", "Singer"), "Sing", "Sing is the common prefix")
        self.assertEqual(pset_4.longest_common_prefix("Medic", "Imedi"), "", "No common prefix")

    def test_binary_to_decimal(self):
        self.assertEqual(pset_4.binary_to_decimal("010"), 2 , "Should be 2")
        self.assertEqual(pset_4.binary_to_decimal("01111"), 15, "Should be 15")
        self.assertEqual(pset_4.binary_to_decimal("1011111"), 95, "Should be 95")

    def test_uncompresssed(self):
        self.assertEqual(pset_4.uncompressed("1S1I6U"), "SIUUUUUU", 'Should be "SIUUUU"')
        self.assertEqual(pset_4.uncompressed("0a2b0c"), "bb", 'Should be "bb"')
        self.assertEqual(pset_4.uncompressed("3x1Y2z"), "xxxYzz", 'Should be "xxxYzz"')

    def test_get_base_counts(self):
        self.assertEqual(pset_4.get_base_counts("AAACCCG"), [3, 3, 1, 0], "Should be [3, 3, 1, 0]")
        self.assertEqual(pset_4.get_base_counts("ACCCCCGGGGGTT"), [1, 5, 5, 2], "Should be [1, 5, 5, 2]")
        self.assertEqual(pset_4.get_base_counts("AAACCCa"), [], "Should be []")

if __name__ == '__main__':
    unittest.main()