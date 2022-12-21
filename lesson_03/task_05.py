from random import randint


def fibo(treshold):
    precending = 0
    following = 1
    lst = [precending, following]

    for i in range(treshold-1):
        next_element = precending + following
        precending, following = following, next_element
        lst.append(next_element)

    return lst


def nega_fibo(fibo_lst):
    fibo_lst = fibo_lst[1:]
    for n in range(1, len(fibo_lst), 2):
        fibo_lst[n] *= -1
    return fibo_lst[::-1]


limit = randint(3, 15)
fibo_direct = fibo(limit)
fibo_reverse = nega_fibo(fibo_direct)

print(fibo_reverse + fibo_direct)
