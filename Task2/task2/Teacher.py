from account import Account


class Teacher(Account):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.type = 'Teacher'

    def show_students(self, course):
        pass

    def show_courses(self):
        pass

    def set_score(self, course, student, score):
        pass

    def get_score(self, course, student):
        pass

    def do_command(self, command):
        pass

    def help(self):
        print('show course #查看教授课程\n'
              'show student #查看学生\n'
              'show score #查看学生成绩\n')
