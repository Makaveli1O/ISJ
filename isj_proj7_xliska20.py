#!/usr/bin/env python3

import collections


def log_and_count(counts, key=None):
    def decorator(func):
        def called_with(*args, **kwargs):
            counts[key if key else func.__name__] += 1
            print(f'called {func.__name__} with {args} and {kwargs}')

        return called_with

    return decorator

def test():
    my_counter = collections.Counter()

    @log_and_count(key = 'basic functions', counts = my_counter)
    def f1(a, b=2):
        return a ** b

    @log_and_count(key = 'basic functions', counts = my_counter)
    def f2(a, b=3):
        return a ** 2 + b

    @log_and_count(counts = my_counter)
    def f3(a, b=5):
        return a ** 3 - b

    f1(2)
    f2(2, b=4)
    f1(a=2, b=4)
    f2(4)
    f2(5)
    f3(5)
    f3(5,4)

    print(my_counter)

if __name__ == '__main__':
    test()