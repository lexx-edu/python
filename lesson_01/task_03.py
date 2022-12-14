def input_coordinates(axis):
    result = 0
    while result == 0:
        result = int(input(f'Введите {axis} != 0: '))
    return result


def quarter(x, y):
    if y > 0:
        return 1 if x > 0 else 4
    else:
        return 2 if x > 0 else 3


X = input_coordinates('X')
Y = input_coordinates('Y')

print(f'\nx = {X}; y = {Y} -> четверть: {quarter(X, Y)}')
