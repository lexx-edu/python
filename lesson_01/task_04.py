quarters = {
    1: 'x>0, y>0',
    2: 'x>0, y<0',
    3: 'x<0, y<0',
    4: 'x<0, y>0'
}

quarter = 0
while quarter not in range(1, 5):
    quarter = int(input('Введите номер четверти координатной плоскости: '))

print(f'\nЧетверть:\t{quarter}\nДопустимо:\t{quarters[quarter]}')
