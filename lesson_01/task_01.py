day = 0

while day not in range(1, 8):
    day = int(input('Введите номер дня недели (1 - 7): '))

answer = 'Выходной' if day > 5 else 'Рабочий'
print(f'{day} -> {answer}')
