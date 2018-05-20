from account import Account


class Admin(Account):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.type = 'Admin'

    def help(self):
        print('add user #添加用户\n'
              'del user #删除用户\n'
              'add school #添加学校\n'
              'del school #删除学校\n'
              'add course #添加课程\n'
              'del course #删除课程\n'
              'add teacher #添加老师\n'
              'del teacher #删除老师\n')

    def do_command(self, command):
        pass

