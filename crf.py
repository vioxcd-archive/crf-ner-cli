import warnings

warnings.filterwarnings('ignore')  # some class not in test_case (zero division)
								   # crfsuite passing labels to classification_report

from utils.load_data import load
from utils.model import model
from utils.preprocess import create_features

DIR_PATH = 'data'

if __name__ == '__main__':
	data = load(DIR_PATH)
	Xf, y = create_features(data)

	f1_score, report = model(Xf, y, .3)

	print(f'f1_score: {f1_score}')
	print(f'report:\n{report}')
