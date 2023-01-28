TAKE_MAX = 28


def step_prepare(rec, user_step):
    step = int(user_step)
    status, remains = list(map(int, rec.split(';')))
    return check_step(step, status, remains)


def check_step(step, status, remains):
    if not 0 <= step <= TAKE_MAX:
        answer = (
            "Напомню правила: брать можно от одной до 28 конфет. Надо бы переходить",
            status,
            remains,
        )
    else:
        remains = remains - step
        answer = step_strategy(step, status, remains)

    return answer


def step_strategy(step, status, remains):
    if 0 < remains <= TAKE_MAX:
        return f'Я забрал {remains} и победил.', status, 0
    elif remains == 0:
        return f'Мне нечего забирать. Ваша победа.', status,  0
    elif status == 0:
        answer = remains % (TAKE_MAX + 1)
    else:
        answer = TAKE_MAX + 1 - step
    remains = remains - answer
    answer = f'Я забираю {answer}. Осталось {remains}'
    return answer, status, remains
