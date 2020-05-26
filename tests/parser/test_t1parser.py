import unittest

from tlr.fixtures import temperature1
from tlr.parser import T1Parser
from tlr.tests.utils import format_as_str, list_to_dict, stringify_dict
from tlr.utils import get_value_or_none


class ParserTest(unittest.TestCase):
    """Test temperature1 parser."""

    def test_parser_as_list(self):
        data_parser = T1Parser()
        for index, string in enumerate(temperature1.raw_data):
            data = data_parser.parse_as_list(string)

            for i, item in enumerate(data):
                first = format_as_str(item)
                second = temperature1.clean_data[index][i]
                self.assertListEqual(first, second)

    def test_parse_as_dict(self):
        data_parser = T1Parser()
        for index, string in enumerate(temperature1.raw_data):
            data = data_parser.parse_as_dict(string)

            for i, item in enumerate(data):
                first = stringify_dict(item)
                second = list_to_dict(
                    temperature1.clean_data[index][i], data_parser.fields)
                self.assertDictEqual(first, second)


if __name__ == '__main__':
    unittest.main()
