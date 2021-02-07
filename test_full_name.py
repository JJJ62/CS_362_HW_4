import unittest
import full_name

class TestConcatenate(unittest.TestCase):
    def test_cat_name(self):
        result = full_name.str_cat("Jawad", "Alamgir")
        self.assertEqual(result, "Jawad Alamgir")
    def test_cat_num(self):
        result = full_name.str_cat(12, 13)
        self.assertEqual(result, "12 13")
    def test_cat_none(self):
        result = full_name.str_cat("", "")
        self.assertEqual(result, " ")