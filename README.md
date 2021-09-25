# NER-CRF runner

Most of the code is taken from [Akshayc1](https://github.com/Akshayc1/named-entity-recognition).

This app **is not finished (yet).** I was planning to made this usable from cli (like, you can pass `--test_size` and `--random-seed` parameters to it). But, I changed my mind and made the complete program in an unpublished notebook instead.

## Setup

`pip3 install -r requirements.txt`

or

`conda install --file requirements.txt`

## Run Test

`python3 -m unittest discover -s tests`

## TODO

1. typing: use types
2. argparse: get correct argument passed
3. random seed: check the effect of random seeds
