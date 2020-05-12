import re
import abc

from .utils import force_str


class ParserError(Exception):
    pass


class BaseParser(object):
    """
    Base parser object to parse telnet data.
    """

    fields = []

    @abc.abstractmethod
    def parse(self, s, **kwargs):
        pass

    def parse_as_list(self, s,
                      delimiter=',',
                      converter=float,
                      **kwargs):
        """
        Parse string s as list. Empty value will be discarded. If converter is
        not None, each value in the list will be converted using the converter
        function.
        """
        cleaned_data = []
        data = self.parse(s, **kwargs).split(delimiter)
        for item in data:
            d = []
            for field in item:
                if not field:
                    continue

                if converter is not None:
                    try:
                        value = converter(field)
                    except ValueError:
                        value = None
                else:
                    value = force_str(field)

                d.append(value)
            cleaned_data.append(d)
        return cleaned_data

    def parse_as_dict(self, s, **kwargs):
        """
        Parse string s as dictionary. Return truncated version if fields length
        less than or greater than list parsed.
        """
        if not self.fields:
            raise ParserError(
                'Parsing as dictionary requires fields to be set')

        data = self.parse_as_list(s, **kwargs)

        def get_value_or_none(data, index):
            try:
                return data[index]
            except IndexError:
                return None

        return dict([
            (k, get_value_or_none(data, i))
            for i, k in enumerate(self.fields)
        ])


class TParser(BaseParser):

    regex = re.compile(r'')

    def parse(self, s, **kwargs):
        return self.regex.findall(s)


class T0Parser(TParser):

    regex = re.compile(r'.*#03\s(?P<data>.*)\r')
    fields = [
        'timestamp',
        'temperature1',
        'temperature2',
        'temperature3',
        'temperature4',
        'battery_voltage',
    ]


class T1Parser(TParser):

    regex = re.compile(r'.*#01\s(?P<data>.*)\r')
    fields = ['timestamp', 'temperature', ]


class T2Parser(BaseParser):

    regex = re.compile(r'.*#02\s(?P<data>.*)\r')
    fields = ['timestamp', 'temperature', ]


class EParser(BaseParser):

    regex = re.compile(r'.*TLR0101256\s(?P<data>.*)\r')
    fields = [
        'timestamp',
        'co2_min',
        'co2_max',
        'co2_avg',
        'temperature_min',
        'temperature_max',
        'temperature_avg',
        'humidity_min',
        'humidity_max',
        'humidity_avg',
        'input_battery_voltage',
    ]

    def parse(self, s, **kwargs):
        return self.regex.findall(s)
