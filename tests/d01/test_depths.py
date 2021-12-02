from unittest import TestCase
from unittest.mock import Mock

from ..common import fixture_path

from aoc.d01.depths import Depths


class TestDepths(TestCase):
    def setUp(self):
        self.script_path = 'ignored/path/to/script'

    def test_requires_input_path_to_be_present(self):
        depths = Depths([self.script_path], Mock())
        self.assertEqual(depths.get(), [])

    def test_informs_user_that_path_is_not_present(self):
        mock = Mock()
        Depths([self.script_path], mock).get()
        mock.print_missing_input_error.assert_called_once()

    def test_requires_input_path_to_be_valid(self):
        depths = Depths([self.script_path, None], Mock())
        self.assertEqual(depths.get(), [])

    def test_informs_user_that_path_is_not_valid(self):
        mock = Mock()
        Depths([self.script_path, None], mock).get()
        mock.print_missing_input_error.assert_called_once()

    def test_requires_input_file_to_exist(self):
        depths = Depths([self.script_path, self.input('inexistent')], Mock())
        self.assertEqual(depths.get(), [])

    def test_informs_user_that_file_is_missing(self):
        mock = Mock()
        Depths([self.script_path, self.input('inexistent')], mock).get()
        mock.print_missing_file_error.assert_called_once()

    def test_requires_input_contents_to_be_valid(self):
        argv = [self.script_path, self.input('invalid_input_words')]
        depths = Depths(argv, Mock())
        self.assertEqual(depths.get(), [])

    def test_informs_user_that_contents_are_not_valid(self):
        mock = Mock()
        argv = [self.script_path, self.input('invalid_input_words')]
        Depths(argv, mock).get()
        mock.print_invalid_number_error.assert_called_once()

    def test_does_not_support_empty_lines_in_input(self):
        argv = [self.script_path, self.input('invalid_input_empty_line')]
        depths = Depths(argv, Mock())
        self.assertEqual(depths.get(), [])

    def test_informs_user_that_empty_line_contents_are_not_valid(self):
        mock = Mock()
        argv = [self.script_path, self.input('invalid_input_empty_line')]
        Depths(argv, mock).get()
        mock.print_invalid_number_error.assert_called_once()

    def test_gets_the_depths_as_a_list(self):
        depths = Depths([self.script_path, self.input('valid_input')], Mock())
        expected = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(depths.get(), expected)

    def input(self, filename):
        return fixture_path('d01', filename)
