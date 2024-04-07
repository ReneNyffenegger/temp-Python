#!/usr/bin/env python3

# Alreeady on 
#  notes - development/languages/Python/standard-library/concurrent/futures/index

from concurrent.futures import ThreadPoolExecutor
import time
import random

items = [1, 2, 3, 4, 5, 6, 7, 8]

def f(item):

    r = random.uniform(0.05, 0.50)

    print(' ' * item + 'S')  # Start
    for i in range(5):   
          print(' ' * item + '.')
          time.sleep(r)

    print(' ' * item + 'F')  # Finished
    


with ThreadPoolExecutor(max_workers=3) as executor:
     executor.map(f, items)
