def step_prepare(rec, user_step):
    step = int(user_step)
    return check_step(step, *rec)


def check_step(step, remains, take_max, status):
    if not 0 <= step <= take_max:
        answer = (
           f'Напомню правила: брать можно от одной до {take_max} конфет. Надо бы переходить', remains, take_max, status)
    else:
        remains = remains - step
        answer = step_strategy(step, status, remains, take_max)

    return answer


def step_strategy(step, status, remains, take_max):
    if 0 < remains <= take_max:
        return f'Я забрал {remains} и победил.', 0, take_max, status
    elif remains == 0:
        return f'Мне нечего забирать. Ваша победа.', 0, take_max, status
    elif status == 0:
        answer = remains % (take_max + 1)
        status = 1
    else:
        answer = take_max + 1 - step
    remains = remains - answer
    answer = f'Я забираю {answer}. Осталось {remains}'
    return answer, remains, take_max, status
