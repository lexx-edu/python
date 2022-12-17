from random import randint


def get_index(limit):
    return randint(0, limit)


def shuffle_list(lst_source):
    lngt = len(lst_source)
    result = [None] * lngt
    for i in lst_source:
        while True:
            index = get_index(lngt-1)
            if result[index] is None:
                result[index] = i
                break
    return result


n = randint(0, 100)
lst = [randint(0, 100) for i in range(n)]
print(lst)
print(shuffle_list(lst))
