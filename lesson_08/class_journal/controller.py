class Journal:
    def __init__(self, interface, backend):
        self.interface = interface
        self.backend = backend
        self.status = False

        self.entrypoint()

    def entrypoint(self):
        self.interface
        while not self.status:
            user_select = self.interface.run_menu()
            self.user_selection_parser(user_select)


    def user_selection_parser(self, value):
        if value == 'm':
            self.interface.print_help()

        elif value == '1':
            self.select_journal()

        elif value == '2':
            self.select_course()

        elif value == '3':
            self.rank_table()

        elif value == '4':
            self.call_to_board()

        elif value == '5':
            self.add_student()

        elif value == '6':
            self.add_course()

        elif value == '7':
            self.save()

        elif value == '8':
            self.create_journal()

        elif value == '0':
            self.status = True

    def create_journal(self):
        journal_name = \
            self.interface.get_free_text('Введите класс для которого создается журнал: ')
        self.backend.create_journal_file(journal_name)

    def select_journal(self):
        string = 'Введите код журнала: '
        current_files = self.backend.get_files()
        select_journal = self.interface.selector(current_files, string)
        self.backend.set_journal(current_files[select_journal])

    def add_student(self):
        name = self.interface.get_free_text('Введите имя новенького: ')
        self.backend.add_student(name)

    def save(self):
        self.backend.save_file()

    def add_course(self):
        course = self.interface.get_free_text('Введите название нового предмета: ')
        self.backend.add_course(course)

    def select_course(self):
        string = 'Введите код курса: '
        courses = self.backend.get_courses()
        course = self.interface.selector(courses, string)
        self.backend.set_context(courses[course])

    def call_to_board(self):
        string = 'Введите код студента: '
        students = self.backend.get_students()
        student = self.interface.selector(students, string)
        score = 0
        while 1 > score or score > 5 :
            score = self.interface.get_free_text('Поставьте оценку: ')
            score = int(score)
        self.backend.add_score(student, score)

    def rank_table(self):
        table = self.backend.get_rank_table()
        self.interface.print_table(table)



