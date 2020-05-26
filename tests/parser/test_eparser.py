import unittest

from tlr.fixtures import emission
from tlr.parser import EParser
from tlr.tests.utils import format_as_str, list_to_dict, stringify_dict
from tlr.utils import force_str, get_value_or_none


class ParserTest(unittest.TestCase):
    """Test CO2 emission parser."""

    def test_parser_as_list(self):
        data_parser = EParser()
        for index, string in enumerate(emission.raw_data):
            data = data_parser.parse_as_list(
                force_str(string, errors='backslashreplace'), delimiter=' ')

            for i, item in enumerate(emission.clean_data[index]):
                first = format_as_str(data[i])
                second = emission.clean_data[index][i]
                self.assertListEqual(first, second)

    def test_parse_as_dict(self):
        data_parser = EParser()
        for index, string in enumerate(emission.raw_data):
            data = data_parser.parse_as_dict(
                force_str(string, errors='backslashreplace'), delimiter=' ')

            for i, item in enumerate(emission.clean_data[index]):
                first = stringify_dict(data[i])
                second = list_to_dict(
                    emission.clean_data[index][i], data_parser.fields)
                self.assertDictEqual(first, second)


if __name__ == '__main__':
    unittest.main()
