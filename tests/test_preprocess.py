import unittest

from utils.preprocess import create_features, sent2labels  # , split


class TestPreprocess(unittest.TestCase):
	def setUp(self):
		self.data = [
			[('A', 'O'), ('B', 'O'), ('C', 'O')],
			[('D', 'O'), ('E', 'O'), ('F', 'O')],
			[('K', 'O'), ('L', 'O'), ('M', 'O')],
			[('N', 'O'), ('O', 'O'), ('P', 'O')],
		]

	def test_create_label_after_loading_data(self):
		example_sentence = self.data[0]
		expected = ['O', 'O', 'O']

		output = sent2labels(example_sentence)

		self.assertIsInstance(output, list)
		self.assertEqual(len(output), len(example_sentence))
		self.assertCountEqual(output, expected)
	
	def test_create_features_after_loading_data(self):
		output_Xf, output_y = create_features(self.data)

		self.assertIsInstance(output_Xf, list)
		self.assertIsInstance(output_y, list)

		feature = output_Xf[0][0]
		self.assertIsInstance(feature, dict)

if __name__ == '__main__':
	unittest.main()
