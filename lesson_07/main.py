from phone_book.controller import entrypoint
from sys import argv

if __name__ == '__main__':
    config_path = argv[1]
    entrypoint(config_path)
