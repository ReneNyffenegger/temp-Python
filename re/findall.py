#!/usr/bin/python
import re

parts = 'foo, bar, baz, etc'

for part in re.findall('(\w+) *(?:,|$)', parts):
    print(part)
