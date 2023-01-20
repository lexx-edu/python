HELP_OPTIONS = {
    'm': 'Помощь (этот раздел)',
    '1': 'Показать все контакты',
    '2': 'Новый контакт',
    '3': 'Изменить контакт',
    '4': 'Удалить контакт',
    '5': 'Найти контакт',
    '6': 'Выйти из программы'
}

def print_help():
    print('\nСписок команд:')
    for key, value in HELP_OPTIONS.items():
        print(f'\t{key}: {value}')


def print_phone_list(phone_list):
    for i in phone_list:
        print_contact(i.split(';'))


def print_contact(contact):
    print()
    print('Имя:', ' '*3, contact[0])
    print('Телефон:', contact[1])


def print_action(action_type):
    print(f'\n{action_type}:')


def print_error():
    print('\nЧто-то пошло не так')


def run_menu():
    print()
    user_select = input("Команда (m для справки): ")
    return user_select


def get_name():
    name = input('Введите имя:   ')
    return name


def get_number():
    phone = input('Введите номер: ')
    return phone