#!/usr/bin/env python3

#  https://discuss.python.org/t/lazy-collection-of-iterables-for-concurrent-futures-executor-map/21045

from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import time

start = time.monotonic()

def log(stage, i):
    print("{stage} {i} after {s} seconds".format(stage=stage, i=i, s=time.monotonic()-start))

def slow_producer(i):
    time.sleep(2)
    return i

def slow_processor(i):
    time.sleep(2)
    log("Processed", i)
    return i

def producer_pool():
    with PoolExecutor(max_workers=2) as executor_produce:
        for i in executor_produce.map(slow_producer, range(12)):
            log("Produced", i)
            yield i
