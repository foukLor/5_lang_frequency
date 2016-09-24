import sys
from collections import Counter
import os
import re

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r',encoding = 'utf-8') as file:
        data = file.read()
    return data

def get_most_frequent_words(text):
    print(Counter(re.split('\W+',data.lower())).most_common()[:10])


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        exit("Usage:")
    data  = load_data(sys.argv[1])
    if not data:
        exit("Usage:")
    get_most_frequent_words(data)
