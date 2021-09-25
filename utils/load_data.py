import os
from collections import namedtuple


def load_paths(DIR_PATH):
	files = os.listdir(DIR_PATH)
	
	if len(files) == 0:
		raise FileNotFoundError
	
	files = [os.path.join(DIR_PATH, file_) for file_ in files]

	return files

def process_strings(as_strings):
	as_list = as_strings.split('\n')
	word_ner = []  # [[(word, ner), (word, ner)], [ sentence ]]
	sentence = []  # [(word, ner), (word, ner)]

	for row in as_list:
		if row:  # akhir kalimat ditandai karakter newline
			word, ner = row.split(' ')
			sentence.append((word, ner))
		else:
			word_ner.append(sentence)
			sentence = []  # buat kalimat baru
	
	return word_ner

def load_data(FILE_PATHS):
	data = []

	for fp in FILE_PATHS:
		with open(fp, 'r', encoding='ISO-8859-1') as f:
			as_strings = f.read()
			data.extend(process_strings(as_strings))

	return data

# PATH = os.path.abspath('/home/uchan/code/fun/crf_cli/tests/test_data')
PATH = os.path.abspath('/home/uchan/code/fun/crf_cli/data')
paths = load_paths(PATH)
result = load_data(paths)

print(len(result))
