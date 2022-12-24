def prepare_string(string):
    string = string.strip(). \
                replace(' ', ''). \
                replace('=0', ''). \
                replace('+', ' '). \
                replace('-', ' -'). \
                replace(' -x', ' -1*x'). \
                replace(' x', ' 1x'). \
                split()
    return string


def split_key_value(string):
    string = string.split('*', 1)
    if len(string) < 2:
        string.append('')
    return string


def read_coeffs(polynom: str):
    polynom = prepare_string(polynom)
    poly_dict = {}

    for i in polynom:
        value, key = split_key_value(i)
        if poly_dict.get(key) is None:
            # Сделал на случай, если придет неправильно сформированный полином
            # Знаю, что коэффициенты могут быть дробными, но
            poly_dict[key] = [int(value)]
        else:
            poly_dict[key].append(int(value))

    return poly_dict


def create_string(degrees, coeff):
    if (coeff > 1 or coeff < -1) and degrees != '':
        return str(coeff) + '*' + degrees
    elif degrees == '':
        return str(coeff)
    elif coeff == 1:
        return degrees
    elif coeff == -1:
        return '-' + degrees
    else:
        return 'ОШИБКА - чего-то не учел'


def create_polynom(poly_dict):
    order = [i for i in poly_dict]
    order.sort()

    string = []
    for key in order[::-1]:
        value = poly_dict[key]
        string.append(create_string(key, value))

    string = '+'.join(string).replace('+-', ' - ').replace('+', ' + ')
    string += ' = 0'
    return string.strip()


def poly_sum(A, B):
    new_keys = list(set([i for i in A] + [i for i in B]))
    sum_poly_dict = {}

    for i in new_keys:
        sum_poly_dict[i] = []
        sum_poly_dict[i].append(sum(A.get(i)) if A.get(i) is not None else 0)
        sum_poly_dict[i].append(sum(B.get(i)) if B.get(i) is not None else 0)
        sum_poly_dict[i] = sum(sum_poly_dict[i])

    return create_polynom(sum_poly_dict)


with open('./polynom.txt', 'r') as read_file:
    a, b = read_file.readline(), read_file.readline()

a = read_coeffs(a)
b = read_coeffs(b)

result = poly_sum(a, b)
with open('./polysum.txt', 'a') as write_file:
    write_file.write(result + '\n')
