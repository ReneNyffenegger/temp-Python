#!/usr/bin/env python3

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
    

def filter_items():
    for item in slow_item_generator():
        if item % 2 == 0:
           yield item
        
    

with ThreadPoolExecutor(max_workers=3) as executor:
     executor.map(f, filter_items())
