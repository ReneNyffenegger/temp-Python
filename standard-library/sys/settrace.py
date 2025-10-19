#!/usr/bin/env python3

# See also https://pymotw.com/3/sys/tracing.html

import sys

def trace_function(frame, event, arg):

    code = frame.f_code
    print(f"{code.co_filename}: {frame.f_lineno} - {code.co_name}")
#   print(frame)
#   print(event)
#   print(arg)
#   if time.time() - start > TOTAL_TIMEOUT:
#       raise Exception('Timed out!')

    return trace_function


def b(i):
    print(f'i = {i}')

def a():
    x = 7
    y = 6
    b(x*y)


sys.settrace(trace_function)
a()
