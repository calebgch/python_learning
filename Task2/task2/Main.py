import data
from user_data import UserData
from account import Account
from admin import Admin
from teacher import Teacher
from student import Student


def init():
    admin = Admin('admin', 'passw0rd')
    teacher = Teacher('teacher', 'passw0rd')
    student = Student('student', 'passw0rd')
    user_list = [admin, teacher, student]
    data.save('user', user_list)


def login():
    username = input("输入用户名:")
    password = input("输入密码:")
    return user_data.login(username, password)


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
    user_data = UserData()
    command = ""

    account = login()
    while account is None:
        account = login()
    print("成功登录")

    while command != "quit" and command != "exit":
        command = input(">>")
        if command == 'help':
            account.help()
            #print_help(account.type)

        print("command: "+command)
        account.do_command(command)




