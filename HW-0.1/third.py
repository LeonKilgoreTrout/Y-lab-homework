def gen5(ceil: int):
    for i in range(0, ceil, 5):
        yield i

gen5(9)

def zeros(n: int):
    for i in gen5(n):
        
# assert zeros(0) == 0
# assert zeros(6) == 1
# assert zeros(30) == 7
#
# print(zeros(1000))