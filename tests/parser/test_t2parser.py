import unittest

from tlr.fixtures import temperature2
from tlr.parser import T2Parser
from tlr.tests.utils import format_as_str, list_to_dict, stringify_dict
from tlr.utils import decode_string, get_value_or_none


class ParserTest(unittest.TestCase):
    """Test temperature2 parser."""

    def test_parser_as_list(self):
        data_parser = T2Parser()
        for index, string in enumerate(temperature2.raw_data):
            data = data_parser.parse_as_list(decode_string(string))

            for i, item in enumerate(data):
                first = format_as_str(item)
                second = temperature2.clean_data[index][i]
                self.assertListEqual(first, second)

    def test_parse_as_dict(self):
        data_parser = T2Parser()
        for index, string in enumerate(temperature2.raw_data):
            data = data_parser.parse_as_dict(decode_string(string))

            for i, item in enumerate(data):
                first = stringify_dict(item)
                second = list_to_dict(
                    temperature2.clean_data[index][i], data_parser.fields)
                self.assertDictEqual(first, second)


if __name__ == '__main__':
    unittest.main()
