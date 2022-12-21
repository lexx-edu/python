from random import randint


def create_list(n=10):
    result = []
    for i in range(n):
        result.append(randint(0, 100))
    return result


lst = create_list()
print(lst, sum(lst[1::2]))
