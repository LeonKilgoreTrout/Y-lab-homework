from typing import Iterable


class CyclicIterator:

    def __init__(self, obj):
        self.obj = obj
        self.gen = self.gen()

    def gen(self):
        while True:
            for i in self.obj:
                yield i

    def __iter__(self):
        return self

    def __next__(self):
        return next(iter(self.gen))


s = CyclicIterator([1, 2, 3])

for i in s:
    print(i)
