#!/usr/bin/python

word_counter = {}

for word in ['foo', 'bar', 'foo', 'foo', 'bar', 'baz', 'baz', 'foo', 'bar']:
    word_counter[word] = word_counter.get(word, 0) + 1

for word, cnt in word_counter.items():
    print('{:2d} x {:s}'.format(cnt, word))

