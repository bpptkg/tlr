import unittest

from tlr.parser import T1Parser
from tlr.utils import force_str


class ParserTest(unittest.TestCase):
    def test_converter(self):
        test_string = (
            b"T#01 56.92,\r\nT#03 88.10,90.62,90.42,29.68,14.39\r\n \r\n C \xfc"
        )
        raw_data = force_str(test_string, errors="backslashreplace")
        data_parser = T1Parser()
        cleaned_data = data_parser.parse_as_list(raw_data, converter=None)
        self.assertEqual(cleaned_data[0][0], "56.92")

        cleaned_data = data_parser.parse_as_dict(raw_data, converter=None)
        self.assertEqual(cleaned_data[0]["temperature"], "56.92")


if __name__ == "__main__":
    unittest.main()
