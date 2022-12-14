def get_approval(symbol):
    result = bool(int(input(f'Введите {symbol} (0=False else=True): ')))
    return result


X = get_approval('X')
Y = get_approval('X')
Z = get_approval('X')

exp_1 = not(X or Y or Z)
exp_2 = not X and not Y and not Z

print(exp_1 == exp_2)
