from unittest import TestCase
from unittest.mock import Mock

from .common import fixture_path

from aoc.file_parser import FileParser


class TestFileParser(TestCase):
    def test_requires_input_file_to_exist(self):
        parser = FileParser(self.input('inexistent'), Mock())
        self.assertEqual(parser.lines(), [])

    def test_informs_user_that_file_is_missing(self):
        mock = Mock()
        FileParser(self.input('inexistent'), mock).lines()
        mock.print_missing_file_error.assert_called_once()

    def test_returns_file_contents_as_list_of_lines(self):
        parser = FileParser(self.input('valid_input'), Mock())
        expected = [
            '199',
            '200',
            '208',
            '210',
            '200',
            '207',
            '240',
            '269',
            '260',
            '263'
        ]
        self.assertEqual(parser.lines(), expected)

    def input(self, filename):
        return fixture_path('d01', filename)
