from data import Data
from admin import Admin
from teacher import Teacher
from student import Student

data = Data()


def init():
    admin = Admin('admin', 'passw0rd')
    teacher = Teacher('teacher', 'passw0rd')
    student = Student('student', 'passw0rd')
    user_list = [admin, teacher, student]
    data.save('user', user_list)


def login():
    username = input("输入用户名:")
    password = input("输入密码:")
    return data.login(username, password)


if __name__ == "__main__":
    init()
    command = ""

    account = login()
    while account is None:
        account = login()
    print("成功登录")

    while command != "quit" and command != "exit":
        command = input(">>")
        if command == 'help':
            account.help()

        print("command: "+command)
        account.do_command(command)




