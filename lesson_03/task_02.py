from random import randint


def create_list(n=10):
    result = []
    for i in range(n):
        result.append(randint(0, 100))
    return result


length = randint(2, 10)
lst = create_list(length)

treshold = int(length / 2)
remainder = length % 2

destination = []
for i, j in zip(lst[:treshold+remainder], lst[:treshold-1:-1]):
    destination.append(i * j)

print('Первичный массив\t', lst)
print('Результат умножения\t', destination)
