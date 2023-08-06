from convert_postifix import convert_to_postifx
import unittest

class test_convert_postifx(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(convert_to_postifx("a + b + c"), "a b + c +")

    def test_complex(self):
        self.assertEqual(convert_to_postifx("a + b + c * d"), "a b + c d * +")

if __name__ == "__main__":
    unittest.main()