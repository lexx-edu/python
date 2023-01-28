from . import backend as bend
from . import game


def help_message():
    help_text = """
    Привет, я умею играть в конфеты, а управлять мной можно через команды
    - /start_game - запустить игру
    - /stop_game - остановить игру
    - /help - эта подказка
    """
    return help_text


def start_game(user):
    response = bend.create_game(user)
    string = \
    f"""
    Начнем игру:
    На столе {response} конфет. За один ход можно взять от 1 до 28.
    Сколько возьмете?
    """
    return string


def stop_game(user):
    bend.delete_game(user)
    return 'Спасибо за игру. Вы - ситльный противник.'


def step_result(user, user_step):
    rec = bend.read_file(user)
    if not rec:
        return 'У нас нет активной игры. Запустите ее с помощью команды /start_game'
    answer_string, *log_data = game.step_prepare(rec, user_step)
    refresh_record(user, log_data)
    return answer_string


def refresh_record(user, line):
    if line[1] == 0:
        bend.delete_game(user)
    else:
        line = ';'.join(map(str, line))
        bend.write_file(user, line)
