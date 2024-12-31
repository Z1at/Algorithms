"""
It caches in memory the result of a function called with a particular set of arguments, which is memoization.

The first time you call caculate_double(5), it will take a second and return 10.
The second time you call the function with the same argument calculate_double(5), it will return 10 instantly.

Adding the cache decorator ensures that if the function has been called recently for a particular value,
it will not recompute that value, but use a cached previous result. In this case, it leads to a
tremendous speed improvement, while the code is not cluttered with the details of caching.
"""


import functools
import time


@functools.cache
def calculate_double(num):
    time.sleep(1) # sleep for 1 second to simulate a slow calculation
    return num * 2


st = time.time()
calculate_double(5)
print(time.time() - st)


st = time.time()
calculate_double(5)
print(time.time() - st)
