import unittest
from unittest.mock import mock_open, patch
from app.io.input import read_file_builtin

class TestFileReading(unittest.TestCase):

    def test_read_file_builtin(self):
        """Test reading a file with built-in open."""
        mock_file_content = "This is a test file."

        with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
            result = read_file_builtin('data/input_builtin.txt')
            self.assertEqual(result, mock_file_content)
            mock_file.assert_called_once_with('data/input_builtin.txt', 'r', encoding='utf-8')

    def test_read_file_builtin_empty(self):
        """Test reading an empty file."""
        mock_file_content = ""

        with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
            result = read_file_builtin('data/test_empty_builtin.txt')
            self.assertEqual(result, mock_file_content)
            mock_file.assert_called_once_with('data/test_empty_builtin.txt', 'r', encoding='utf-8')

    def test_read_file_builtin_nonexistent(self):
        """Test for reading a non-existent file."""
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                read_file_builtin('data/non_existent_file.txt')