#!/usr/bin/python

import re

text = 'foo:bar:baz'

m = re.search('(\w+):(\w+):(\w+)', text)

print('one:   {:s}'.format(m      [1]))
print('two:   {:s}'.format(m.group(2)))
print('three: {:s}'.format(m      [3]))
