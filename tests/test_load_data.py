import os
import tempfile
import unittest

from utils.load_data import load_paths, process_strings


class TestLoadData(unittest.TestCase):
	def test_raise_error_on_data_directory_empty(self):
		with tempfile.TemporaryDirectory() as tmpdir:
			self.assertRaises(FileNotFoundError, load_paths, tmpdir)
	
	def test_correct_path_for_files_in_data_directory(self):
		with tempfile.TemporaryDirectory() as tmpdir:
			TEST_FILENAME = os.path.join(tmpdir, 'test.txt')

			with open(TEST_FILENAME, 'w') as f:
				f.write('something')

			one_file_from_dir = load_paths(tmpdir)[0]
			self.assertEqual(one_file_from_dir, TEST_FILENAME)
	
	def test_data_format_is_as_expected(self):
		"""test processing loaded strings using process_strings"""
		input_format = "A O\nB O\nC O\n\nD O\nE O\nF O\n"
		expected_output = [
			('A', 'O'), ('B', 'O'), ('C', 'O'),
			('D', 'O'), ('E', 'O'), ('F', 'O'),
		]

		output = process_strings(input_format)

		self.assertIsInstance(output, list)
		self.assertNotEqual(len(output), 0)

		instance = output[0]
		self.assertIsInstance(instance, tuple)
		self.assertEqual(len(instance), 2)
		
		self.assertCountEqual(output, expected_output)
			
if __name__ == '__main__':
	unittest.main()
