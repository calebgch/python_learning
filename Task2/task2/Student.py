from account import Account


class Student(Account):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.type = 'Student'

    def register_class(self):
        pass

    def get_courses(self):
        pass

    def do_command(self, command):
        pass


