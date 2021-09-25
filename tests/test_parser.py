import unittest

from utils.parser import create_parser


#  https://stackoverflow.com/a/18161115/8996974
class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = create_parser()

    def test_test_size_is_passed_as_argument(self):
        parsed = self.parser.parse_args(['.3'])
        self.assertEqual(parsed.test_size, .3)

    def test_random_seed_is_passed_as_argument(self):
        parsed = self.parser.parse_args(['.3', '--random-seed'])
        self.assertEqual(parsed.random_seed, True)


if __name__ == '__main__':
	unittest.main()
