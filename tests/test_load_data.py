import tempfile
import unittest

from utils.load_data import load_paths


class TestLoadData(unittest.TestCase):

	def test_raise_error_on_data_directory_empty(self):
		with tempfile.TemporaryDirectory() as tmpdir:
			self.assertRaises(FileNotFoundError, load_paths, tmpdir)

if __name__ == '__main__':
	unittest.main()
