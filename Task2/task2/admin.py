from account import Account
from teacher import Teacher
from student import Student

import dataset


class Admin(Account):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.type = 'Admin'
        #self.data_set = Data()

    def help(self):
        print('add user #添加用户\n'
              'del user #删除用户\n'
              'add school #添加学校\n'
              'del school #删除学校\n'
              'add course #添加课程\n'
              'del course #删除课程\n'
              'add teacher #添加老师\n'
              'del teacher #删除老师\n'
              'show user #显示用户')

    def do_command(self, command):
        if command == 'add user':
            self.add_user()
        elif command == 'del user':
            self.del_user()
        elif command == 'add school':
            pass
        elif command == 'del school':
            pass
        elif command == 'add course':
            pass
        elif command == 'del course':
            pass
        elif command == 'add teacher':
            pass
        elif command == 'del teacher':
            pass
        elif command == 'show user':
            self.show_user()
        elif command == 'reset':
            self.reset()

    def reset(self):
        dataset.init()

    def add_user(self):
        new_username = input("输入新用户名:")
        new_password = input("输入密码:")
        new_type = input("输入用户类型:")
        account = self.create_account(new_username, new_password, new_type)
        #ds = Data()
        #ds.add_account(account)
        dataset.add_account(account)

    def del_user(self):
        ds = Data()
        username = input("输入要删除的用户名:")
        #if self.data_set.del_account(username):
        if ds.del_account(username):
            print('用户删除成功')
        else:
            print('用户删除失败')

    def show_user(self):
        #self.data_set.show_account()
        #ds = Data()
        #ds.show_account()
        list = dataset.user_list()
        for account in list:
            print(account.username)

    def create_account(self, username, password, type):
        if type == 'Admin' or type == 'A':
            return Admin(username, password)
        elif type == 'Teacher' or type == 'T':
            return Teacher(username, password)
        elif type == 'Studeng' or type == 'S':
            return Student(username, password)
        else:
            return None
