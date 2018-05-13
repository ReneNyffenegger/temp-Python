#!/usr/bin/python

from collections import Counter


words = ['foo', 'bar', 'foo', 'foo', 'bar', 'baz', 'baz', 'foo', 'bar']

def show_dict(d):
    for word, cnt in d.items():
        print('{:2d} x {:s}'.format(cnt, word))

def count_with_dict():

    word_counter = {}

    for word in words:
        word_counter[word] = word_counter.get(word, 0) + 1

    show_dict(word_counter)
    

def count_with_Counter():
    counted_words = Counter(words)
    show_dict(counted_words)


count_with_dict()
count_with_Counter()
