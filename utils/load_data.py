import os


def load_paths(DIR_PATH):
	files = os.listdir(DIR_PATH)
	
	if len(files) == 0:
		raise FileNotFoundError
	
	files = [os.path.join(DIR_PATH, file_) for file_ in files]

	return files
