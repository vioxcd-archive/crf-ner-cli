import os


def load_paths(DIR_PATH):
	files = os.listdir(DIR_PATH)
	
	if len(files) == 0:
		raise FileNotFoundError
	
	files = [os.path.join(DIR_PATH, file_) for file_ in files]

	return files

def process_strings(as_strings):
	as_list = as_strings.split('\n')
	word_ner_pairs = []

	for word_ner in as_list:
		try:
			word, ner = word_ner.split(' ')
		except ValueError:
			continue

		word_ner_pairs.append((word, ner))

	return word_ner_pairs

def load_data(FILE_PATHS):
	data = []

	for fp in FILE_PATHS:
		with open(fp, 'r', encoding='ISO-8859-1') as f:
			as_strings = f.read()
			data.append(process_strings(as_strings))

	return data

# PATH = os.path.abspath('/home/uchan/code/fun/crf_cli/tests/test_data')
PATH = os.path.abspath('/home/uchan/code/fun/crf_cli/data')
paths = load_paths(PATH)
result = load_data(paths)

print(result)
