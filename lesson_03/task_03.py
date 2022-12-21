from random import randint, random, choice


def get_number():
    is_realis = choice([True, False])
    number = randint(0, 100)
    if is_realis:
        tail = random()
        number = round(number + tail, 3)
    return number


def create_list(n=10):
    result = []
    for i in range(n):
        result.append(get_number())
    return result


length = randint(2, 10)
lst = create_list(length)
print(lst)

max_tail = 0.0
min_tail = 0.0

for i in lst:
    if isinstance(i, int):
        continue

    i = i - int(i)

    if max_tail == 0.0:
        max_tail = i
        min_tail = i
        continue

    if i > max_tail:
        max_tail = i
    elif i < min_tail:
        min_tail = i

if min_tail == max_tail:
    print('Решения нет')
else:
    print(max_tail - min_tail)

