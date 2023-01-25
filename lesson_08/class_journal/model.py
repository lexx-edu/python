import os
import json

class BackEnd:
    def __init__(self, path):
        self.path = path
        self.file = None
        self.data = None
        self.context = None

    def create_journal_file(self, file_name):
        self.set_journal('template.json')
        self.set_journal(file_name + '.json', False)

    def read_file(self):
        path = self.get_path()
        with open(path, 'r') as file:
            raw = file.read()
            self.data = json.loads(raw)

    def save_file(self):
        path = self.get_path()
        raw = json.dumps(self.data)
        with open(path, 'w') as file:
            file.write(raw)

    def get_path(self):
        return os.path.join(self.path, self.file)

    def get_files(self):
        files = os.listdir(self.path)
        files.remove('template.json')
        return files

    def get_courses(self):
        courses = [i for i in self.data['courses']]
        return courses

    def get_students(self):
        students = [i for i in self.data['students']]
        return students

    def get_rank_table(self):
        table = {i:[] for i in self.data['students']}
        scores = zip(self.data['courses'][self.context]['score'],
                     self.data['courses'][self.context]['student'])

        for score, student in scores:
            name = self.data['students'][student]
            table[name].append(score)

        return table

    def set_journal(self, file_name, read=True):
        self.file = file_name
        if read:
            self.read_file()
        else:
            self.save_file()

    def set_context(self, context):
        self.context = context

    def add_student(self, name):
        if self.file is not None:
            self.data['students'].append(name)

    def add_course(self, course_name):
        if self.file is not None:
            self.data['courses'][course_name] = {'score': [], 'student': []}

    def add_score(self, student, score):
        self.data['courses'][self.context]['student'].append(student)
        self.data['courses'][self.context]['score'].append(score)
