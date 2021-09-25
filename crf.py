from utils.load_data import load
from utils.model import model
from utils.preprocess import create_features

DIR_PATH = 'data'

if __name__ == '__main__':
	data = load(DIR_PATH)
	Xf, y = create_features(data)

	# labels = set([tag for ners in y for tag in ners])

	# f1_score, report = model(Xf, y, .3, labels)
	f1_score, report = model(Xf, y, .3)

	print(f'f1_score: {f1_score}')
	print(f'report:\n{report}')
