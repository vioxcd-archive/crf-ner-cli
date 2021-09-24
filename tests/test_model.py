import unittest

from utils.model import model


class TestModel(unittest.TestCase):

	def test_model(self):
		x = model()
		self.assertEqual(x, 2)

if __name__ == '__main__':
	unittest.main()

