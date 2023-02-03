from random import randint

TAKE_MAX_DEFAULT = 28
game_settings = {}
current_game = {}
in_config = []


def set_default(user, take_max=0):
    if user in in_config:
        game_settings[user] = take_max
        in_config.pop(in_config.index(user))
    return 0


def set_in_config(user):
    if user in in_config:
        return 1
    else:
        in_config.append(user)
        return 0


def set_step(user, game):
    current_game[user] = game


def get_in_config(user):
    return user in in_config


def get_game(user):
    game = current_game.get(user)
    if game is None:
        return 1
    else:
        return game


def start_game(user):
    if user in in_config:
        return 2, 0, 0
    game = get_game(user)
    if game == 1:
        max_take = game_settings.get(user, TAKE_MAX_DEFAULT)
        current_game[user] = [randint(TAKE_MAX_DEFAULT + 1, 200), max_take, 0]
        return 0, *get_game(user)
    else:
        return 1, *game


def stop_game(user):
    if current_game.get(user) is not None:
        current_game.pop(user)
    return 0



