import os


def load_paths(DIR_PATH):
	files = os.listdir(DIR_PATH)

	if len(files) == 0:
		raise FileNotFoundError

	return files
