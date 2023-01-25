from class_journal.controller import Journal
from class_journal.view import Interface
from class_journal.model import BackEnd


if __name__ == '__main__':
    data_path = './data'
    interface = Interface()
    backend = BackEnd(data_path)
    learning_day = Journal(interface, backend)