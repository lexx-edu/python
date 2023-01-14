from sys import argv
import re


def action(input_file, output_file):
    input_data = read_file(input_file)

    if input_data[0].isdigit():
        result = uncompress(input_data)
    else:
        result = compress(input_data)

    save_file(output_file, result)

def read_file(input_file):
    with open(input_file, 'r') as file:
        string = file.read()
        if string[-1] == '\n':
            string = string[:-1]
    return string


def compress(input_data):
    counter = 0
    template = input_data[0]
    result = ''

    for i in input_data:
        if i == template:
            counter += 1
            continue

        result += f'{counter}{template}'
        counter = 1
        template = i
    else:
        result += f'{counter}{template}'

    return result

def uncompress(input_data):
    preparing = re.findall('\d*\w', input_data)
    result = ''

    for i in preparing:
        result += int(i[:-1]) * i[-1]

    return result


def save_file(output_file, string):
    with open(output_file, 'w') as file:
        file.write(string)


if __name__ == '__main__':
    input_filename = argv[1]
    output_filename = argv[2]

    action(input_filename, output_filename)
