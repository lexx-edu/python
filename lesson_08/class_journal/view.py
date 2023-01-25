HELP_OPTIONS = {
    'm': 'Помощь (этот раздел)',
    '1': 'Загрузить классный журнал',
    '2': 'Выбрать предмет',
    '3': 'Табель успеваемости по предмету',
    '4': 'Вызвать к доске',
    '5': 'Добавить ученика',
    '6': 'Добавить предмет',
    '7': 'Сохранить изменения',
    '8': 'Создать новый журнал',
    '0': 'Выйти из программы'
}

class Interface:
    def __init__(self):
        self.select_status = None

    @staticmethod
    def run_menu():
        print()
        user_select = input("Команда (m для справки): ")
        return user_select

    @staticmethod
    def print_help():
        print('\nСписок команд:')
        for key, value in HELP_OPTIONS.items():
            print(f'\t{key}: {value}')

    @staticmethod
    def get_free_text(input_string):
        return input(input_string)

    @staticmethod
    def print_selector(selector):
        for n, i in enumerate(selector):
            print(f"{n}: {i.replace('.json', '')}")

    @staticmethod
    def print_table(table):
        for i in table:
            print(i, '\t', table[i])

    def selector(self, selector_list, command_string):
        self.print_selector(selector_list)
        choice = self.get_free_text(command_string)
        return int(choice)