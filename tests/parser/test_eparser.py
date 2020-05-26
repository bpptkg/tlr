import unittest

from tlr.fixtures import emission
from tlr.parser import EParser
from tlr.tests.utils import format_as_str, list_to_dict, stringify_dict
from tlr.utils import decode_string, get_value_or_none


class ParserTest(unittest.TestCase):
    """Test CO2 emission parser."""

    def test_parser_as_list(self):
        data_parser = EParser()
        for index, string in enumerate(emission.raw_data):
            data = data_parser.parse_as_list(
                decode_string(string), delimiter=' ')

            for i, item in enumerate(data):
                first = format_as_str(item)
                second = emission.clean_data[index][i]
                self.assertListEqual(first, second)

    def test_parse_as_dict(self):
        data_parser = EParser()
        for index, string in enumerate(emission.raw_data):
            data = data_parser.parse_as_dict(
                decode_string(string), delimiter=' ')

            for i, item in enumerate(data):
                first = stringify_dict(item)
                second = list_to_dict(
                    emission.clean_data[index][i], data_parser.fields)
                self.assertDictEqual(first, second)


if __name__ == '__main__':
    unittest.main()
