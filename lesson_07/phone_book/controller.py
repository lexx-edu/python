from . import extensions
from . import view
from . import model

DATABASE = ''

def entrypoint(config_path):
    global DATABASE
    status = False

    config = extensions.read_config(config_path)
    DATABASE = config['main']['database']

    while not status:
        user_select = view.run_menu()
        status = user_selection_parser(user_select)


def user_selection_parser(value):
    if value == 'm':
        view.print_help()

    elif value == '1':
        phonebook = model.get_all(DATABASE)
        view.print_phone_list(phonebook)

    elif value == '2':
        view.print_action('Добавить новый контакт')
        name = view.get_name()
        phone = view.get_number()
        new_contact = (name, phone)
        model.append_data(DATABASE, new_contact)

    elif value == '3':
        view.print_action('Изменить существующий контакт')
        name = view.get_name()
        phone = view.get_number()
        new_contact = (name, phone)
        model.replace_data(DATABASE, new_contact)

    elif value == '4':
        view.print_action('Удалить существующий контакт')
        name = view.get_name()
        status = model.delete_data(DATABASE, name)
        if status is None:
            view.print_error()

    elif value == '5':
        name = view.get_name()
        status = model.find_data(DATABASE, name)
        if status is None:
            view.print_error()
        else:
            view.print_contact(status)

    elif value == '6':
        return True

    return False

