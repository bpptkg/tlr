import unittest

from tlr import utils


class UtilsTest(unittest.TestCase):
    def setUp(self):
        self.byte_string = b"TLR0101256 +635.00 +712.00 +669.75 +29.53 +30.01 +29.81 +74.01 +74.44 +74.28 +12.05 \r\n \x16\xfd\xd1=e\x04\x15\x04\x188"

    def test_decode_string(self):
        result = utils.decode_string(self.byte_string)
        self.assertTrue(isinstance(result, bytes))

    def test_force_str_default(self):
        with self.assertRaises(UnicodeDecodeError):
            result = utils.force_str(self.byte_string)

    def test_force_str_backslashreplace(self):
        result = utils.force_str(self.byte_string, errors="backslashreplace")
        self.assertTrue(isinstance(result, str))


if __name__ == "__main__":
    unittest.main()
