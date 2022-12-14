from random import randint
from math import sqrt


def create_pair(start=1, finish=10):
    finish += 1
    x = randint(start, finish)
    y = randint(start, finish)
    return x, y


def distance_calculation(pairs: list = None):
    if pairs is None:
        x1, y1 = create_pair()
        x2, y2 = create_pair()
    else:
        x1, y1, x2, y2 = pairs

    result = round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
    print(f'x1={x1}, y1={y1}; x2={x2}, y2={y2} -> {abs(result)}')


if __name__ == '__main__':
    distance_calculation([7, -5, 1, -1])

