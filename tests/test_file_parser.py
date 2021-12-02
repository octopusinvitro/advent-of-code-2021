from unittest import TestCase
from unittest.mock import Mock

from .common import fixture_path

from aoc.file_parser import FileParser


class TestFileParser(TestCase):
    def setUp(self):
        self.script_path = 'ignored/path/to/script'

    def test_requires_input_path_to_be_present(self):
        parser = FileParser([self.script_path], Mock())
        self.assertEqual(parser.lines(), [])

    def test_informs_user_that_path_is_not_present(self):
        mock = Mock()
        FileParser([self.script_path], mock).lines()
        mock.print_missing_input_error.assert_called_once()

    def test_requires_input_path_to_be_valid(self):
        parser = FileParser([self.script_path, None], Mock())
        self.assertEqual(parser.lines(), [])

    def test_informs_user_that_path_is_not_valid(self):
        mock = Mock()
        FileParser([self.script_path, None], mock).lines()
        mock.print_missing_input_error.assert_called_once()

    def test_requires_input_file_to_exist(self):
        argv = [self.script_path, self.input('inexistent')]
        parser = FileParser(argv, Mock())
        self.assertEqual(parser.lines(), [])

    def test_informs_user_that_file_is_missing(self):
        argv = [self.script_path, self.input('inexistent')]
        mock = Mock()
        FileParser(argv, mock).lines()
        mock.print_missing_file_error.assert_called_once()

    def test_returns_file_contents_as_list_of_lines(self):
        argv = [self.script_path, self.input('valid_input')]
        parser = FileParser(argv, Mock())
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
