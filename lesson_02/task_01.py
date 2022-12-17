def digit_sum(num):
    string = str(num)
    string = string.replace('.', '0')
    result = 0
    for i in string:
        result += int(i)
    return result


while True:
    users_num = input("Введите число: ")
    try:
        users_num = float(users_num)
        break
    except ValueError:
        continue

print(digit_sum(users_num))
