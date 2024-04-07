#!/usr/bin/env python3

# Already on 
#  notes - development/languages/Python/standard-library/concurrent/futures/index

from concurrent.futures import ThreadPoolExecutor
import time
import random

def slow_item_generator():

    for i in range(16):
        yield i
        time.sleep(1)


def f(item):

    r = random.uniform(0.05, 0.50)

    print(' ' * item + 'S')  # Start
    for i in range(5):   
          print(' ' * item + '.')
          time.sleep(r)

    print(' ' * item + 'F')  # Finished
    

with ThreadPoolExecutor(max_workers=3) as executor:
     executor.map(f, slow_item_generator())
