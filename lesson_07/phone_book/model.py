def get_all(path):
    with open(path, 'r') as file:
        data = file.readlines()
    return data


def normalize_data(data):
    return f'{data[0]};{data[1]}\n'


def append_data(path, data):
    data = normalize_data(data)
    with open(path, 'a') as file:
        file.write(data)


def replace_data(path, data):
    delete_data(path, data[0])
    append_data(path, data)


def delete_data(path, data):
    all_data = get_all(path)
    index = find_data(all_data, data, 'index')
    if index is None:
        return None

    all_data.pop(index)
    with open(path, 'w') as file:
        file.writelines(all_data)

    return 'OK'


def find_data(path, data, return_type='data'):
    if isinstance(path, str):
        all_data = get_all(path)
    else:
        all_data = path

    all_data = map(lambda x: x.split(';'), all_data)
    for n, i in enumerate(all_data):
        if i[0] == data:
            return i if return_type == 'data' else n
    return None

