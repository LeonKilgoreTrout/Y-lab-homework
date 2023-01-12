from typing import Dict, Any


cache_dict = {}


def cache(func):
    def wrap(number: int):
        if number in cache_dict.keys():
            print(f'Cached value {cache_dict[number]} returned')
            return cache_dict[number]
        else:
            result = func(number)
            cache_dict[number] = result
            return result
    return wrap


@cache
def multiplier(number: int):
    return number * 2


for i in '123321412':
    print(multiplier(int(i)))
