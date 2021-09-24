import unittest

from utils.preprocess import preprocess


class TestPreprocess(unittest.TestCase):
	def test_preprocess(self):
		x = preprocess()
		self.assertEqual(x, 2)

if __name__ == '__main__':
	unittest.main()
