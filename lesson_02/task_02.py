def progression(n):
    result = []
    for i in range(1, n+1):
        result.append(round((i + 1/i) ** i, 3))
    return result


x = int(input('Введите число: '))
lst = progression(x)
print(', '.join(str(i) for i in lst))
print(sum(lst))
