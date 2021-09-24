import os
import tempfile
import unittest

from utils.load_data import load_data, load_paths


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

if __name__ == '__main__':
	unittest.main()
