from random import randint
from functools import reduce


# def create_list(n=10):
#     result = []
#     for i in range(n):
#         result.append(randint(0, 100))
#     return result
#
# lst = create_list()
# print(lst, sum(lst[1::2]))
#

lst = list(map(lambda x: randint(0, 100), [i for i in range(randint(2, 10))]))

print(lst, reduce(lambda res, x: res + x,
                        map(lambda x: lst[x],
                            [n for n, _ in enumerate(lst) if n % 2 != 0])))
