import unittest

from utils.load_data import load_data


class TestLoadData(unittest.TestCase):

	def test_load_data(self):
		x = load_data()
		self.assertEqual(x, 2)

if __name__ == '__main__':
	unittest.main()
