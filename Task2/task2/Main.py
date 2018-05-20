import pickle
import data
from auth import Auth
from account import Account


def init():
    admin = Account('admin', 'passw0rd', 'Admin')
    teacher = Account('teacher', 'passw0rd', 'Teacher')
    student = Account('student', 'passw0rd', 'Student')
    user_list = [admin, teacher, student]
    data.save('user', user_list)


def login():
    username = input("输入用户名:")
    password = input("输入密码:")
    return auth.login(username, password)


def print_help(type):
    if type == 'Admin':
        print('add user #添加用户\n'
              'del user #删除用户\n'
              'add school #添加学校\n'
              'del school #删除学校\n'
              'add course #添加课程\n'
              'del course #删除课程\n'
              'add teacher #添加老师\n'
              'del teacher #删除老师\n')
    elif type == 'Teacher':
        print('show course #查看教授课程\n'
              'show student #查看学生\n'
              'show score #查看学生成绩\n')
    elif type == 'Student':
        print('register course #报名课程\n'
              'quit course #退出课程\n')


if __name__ == "__main__":
    init()
    auth = Auth()
    command = ""

    account = login()
    while account is None:
        account = login()
    print("成功登录")

    while command != "quit" and command != "exit":
        command = input(">>")
        if command == 'help':
            print_help(account.type)

        print("command: "+command)



