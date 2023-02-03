from . import game
from . import backend


def help_message():
    help_text = """
    Привет, я умею играть в конфеты, а управлять мной можно через команды
    - /set_game - установить лимит забираемых конфет
    - /start_game - запустить игру
    - /stop_game - остановить игру
    - /help - эта подказка
    """
    return help_text


def start_game(user):
    response = backend.start_game(user)
    main_string = \
        f'На столе {response[1]} конфет. За один ход можно взять от 1 до {response[2]}.\n' \
        'Сколько возьмете?'
    if response[0] == 1:
        string = f'Мы уже играем\n'
    elif response[0] == 0:
        string = f'Начнем игру:\n'
    else:
        return 'Вы находитесь в режиме конфигурации игры. Введите максимальное количество конфет для одного хода:'
    return string + main_string


def stop_game(user):
    backend.stop_game(user)
    return 'Спасибо за игру. Вы - ситльный противник.'


def set_max(user):
    in_game = backend.get_game(user)
    if in_game != 1:
        return 'Простите, вы уже играете. Менять параметры хода во время игры нельзя.'
    else:
        backend.set_in_config(user)
        return 'Введите максимальное количество конфет, которое можно забрать за один ход:'


def step_result(user, user_step):
    if backend.get_in_config(user):
        backend.set_default(user, user_step)
        return f'Установлено максимальное количество конфет для 1 хода - {user_step}'
    rec = backend.get_game(user)
    if rec == 1:
        return 'У нас нет активной игры. Запустите ее с помощью команды /start_game'
    answer_string, *log_data = game.step_prepare(rec, user_step)
    refresh_record(user, log_data)
    return answer_string


def refresh_record(user, line):
    if line[0] == 0:
        backend.stop_game(user)
    else:
        backend.set_step(user, line)
