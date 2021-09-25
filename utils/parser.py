import argparse


# https://realpython.com/command-line-interfaces-python-argparse
def create_parser():
	parser = argparse.ArgumentParser(prog='ner crf runner',
									 usage='%(prog)s test_size --random-seed',
									 description='Run CRF model for NER task')

	# positional argument don't use '-' or '--'
	# optinal argument uses them
	parser.add_argument('test_size',
						metavar='test_size',
						type=float,
						help='% of test_size used')
	
	parser.add_argument('--random-seed',
						action='store_true',
						help='whether to seed the model or not')

	return parser
