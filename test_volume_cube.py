import unittest
import volume_cube


class TestVol(unittest.TestCase):
    def test_negative(self):
        result = volume_cube.get_volume(-3)
        self.assertEqual(result, -27)
        result = volume_cube.get_volume(-4)
        self.assertEqual(result, -64)
        result = volume_cube.get_volume(-5)
        self.assertEqual(result, -125)

    def test_positive(self):
        result = volume_cube.get_volume(3)
        self.assertEqual(result, 27)
        result = volume_cube.get_volume(4)
        self.assertEqual(result, 64)
        result = volume_cube.get_volume(5)
        self.assertEqual(result, 125)

    def test_zero(self):
        result = volume_cube.get_volume(0)
        self.assertEqual(result, 0)

    def test_fract(self):
        result = volume_cube.get_volume(3.14)
        self.assertEqual(result, 27)
