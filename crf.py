import sys
import warnings

import numpy as np

warnings.filterwarnings('ignore')  # some class not in test_case (zero division)
								   # crfsuite passing labels to classification_report

from utils.load_data import load
from utils.model import train_model
from utils.parser import create_parser
from utils.preprocess import create_features

DIR_PATH = 'data'

if __name__ == '__main__':
	parser = create_parser()
	parser = parser.parse_args(sys.argv[1:])

	test_size = parser.test_size
	random_seed = parser.random_seed

	if random_seed:
		np.random.seed(42)

	data = load(DIR_PATH)
	Xf, y = create_features(data)

	f1_score, report = train_model(Xf, y, test_size)

	print(f'f1_score: {f1_score}')
	print(f'report:\n{report}')
