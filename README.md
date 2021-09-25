# NER-CRF runner

Most of the code is taken from [Akshayc1](https://github.com/Akshayc1/named-entity-recognition).

At first, I write this so that my friend can easily use it from the command line. She ended up using the notebook version, and I still finish this app anyway, because it's my first time learning TDD (testing notes can be found [here](https://github.com/vioxcd/testing-notes)), put models from notebooks into modular form, and try out [argparse](https://realpython.com/command-line-interfaces-python-argparse).

## Setup

`pip3 install -r requirements.txt`

or

`conda install --file requirements.txt`

## Run Test

`python3 -m unittest discover -s tests`

## Using The Program

1. Create a `data` directory in your root project path.
2. Under the `data` directory, put your `.txt` word-ner pair documents. (check out `tests/test_data` for format example)
3. Run the program using:
   - `python3 crf.py <test_size> [--random-seed]`
   - `python3 crf.py .3  # 70 train-30 test`
   - `python3 crf.py .3 --random-seed  # determined result`
