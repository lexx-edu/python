import os
from random import randint

TAKE_MAX = 28


def get_path(user):
    if not os.path.exists('./data'):
        os.mkdir('./data')
    user = str(user)
    return os.path.join('./data', user+'.csv')


def get_capacity():
    return randint(100, 200)


def read_file(user):
    path = get_path(user)
    if not os.path.exists(path):
        return False
    with open(path, 'r') as file:
        line = file.read()
    return line


def write_file(user, line):
    path = get_path(user)
    with open(path, 'w') as file:
        file.write(line)


def create_game(user):
    capacity = get_capacity()
    line = f'0;{capacity}'
    write_file(user, line)
    return capacity


def delete_game(user):
    path = get_path(user)
    if os.path.exists(path):
        os.remove(path)
