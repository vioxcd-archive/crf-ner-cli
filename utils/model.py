from sklearn.model_selection import train_test_split
from sklearn_crfsuite import CRF
from sklearn_crfsuite.metrics import flat_classification_report, flat_f1_score


def train_model(Xf, y, test_size):
	X_train, X_test, y_train, y_test = train_test_split(Xf, y, test_size=test_size)

	crf = CRF(algorithm = 'lbfgs',
         c1 = 0.1,
         c2 = 0.1,
         max_iterations = 100,
         all_possible_transitions = False)

	crf.fit(X_train, y_train)
	y_pred = crf.predict(X_test)

	f1_score = flat_f1_score(y_test, y_pred, average = 'weighted')
	report = flat_classification_report(y_test, y_pred)

	return f1_score, report
