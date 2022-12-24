from random import randint


def create_coeff(min_limit=-100, max_limit=100):
    return randint(min_limit, max_limit)


def get_criterions(k):
    # Решил, что нужно возвращать степени многочлена последовательно
    # от большей к меньшей, поэтому - пришлось брать списки

    coeffs = []
    degrees = []

    for i in range(0, k+1)[::-1]:
        if i > 1:
            degrees.append(f'*x**{i}')
        elif i == 1:
            degrees. append('*x')
        else:
            degrees.append('')
        coeffs.append(create_coeff())
    return coeffs, degrees


def create_polynom(k=5):
    coeffs, degrees = get_criterions(k)
    eq = []

    for i in zip(coeffs, degrees):
        if i[0] == 0:
            continue
        eq.append(str(i[0]) + i[1])

    eq = '+'.join(eq).replace('+-', ' - ').replace('+', ' + ').replace(' 1*', ' ')
    return eq + ' = 0'


polinom = create_polynom()
with open('./polynom.txt', 'a') as polinom_storage:
    polinom_storage.write(polinom + '\n')
