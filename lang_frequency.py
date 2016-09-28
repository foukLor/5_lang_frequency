import sys
from collections import Counter
import os
import re


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r',encoding = 'utf-8') as data_file:
        data = data_file.read()
    return data

def get_most_frequent_words(text):
    NUM_OF_WORDS = 10
    print(Counter(re.split('\W+',data.lower())).most_common()[:NUM_OF_WORDS])


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        exit("Usage:python3.5 lang_frequency.py path_do_data")
    data  = load_data(sys.argv[1])
    if not data:
        exit("data is unvalid")
    print("10 most frequent words from this file")
    get_most_frequent_words(data)
