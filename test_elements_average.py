import unittest
import elements_average

class TestAvg(unittest.TestCase):
    def test_avg_2(self):
        result = elements_average.get_average([2, 4])
        self.assertEqual(result, 3)
    def test_avg_6(self):
        result = elements_average.get_average([2, 4, 6, 8, 12, 16])
        self.assertEqual(result, 8)
    def test_avg_12(self):
        result = elements_average.get_average([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
        self.assertEqual(result, 16)

    def test_avg_neg(self):
        result = elements_average.get_average([2, -4, 6, 8, 12, -16])
        self.assertEqual(result, 1)

    def test_avg_zero(self):
        result = elements_average.get_average([0, 0, 0, 0, 0, 0])
        self.assertEqual(result, 0)
        result = elements_average.get_average([0, 1, 0, 4, 0, 4])
        self.assertEqual(result, 1)