import sys
from collections import Counter
import os
import re

NUM_OF_WORDS = 10

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r',encoding = 'utf-8') as data_file:
        data = data_file.read()
    return data

def get_most_frequent_words(text):
    print(Counter(re.split('\W+',data.lower())).most_common()[:NUM_OF_WORDS])


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        exit("Usage:")
    data  = load_data(sys.argv[1])
    if not data:
        exit("data is unvalid")
    print("{0} most frequent words from this file".format(NUM_OF_WORDS))
    get_most_frequent_words(data)
