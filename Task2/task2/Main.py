from data import Data
#from admin import Admin
#from teacher import Teacher
#from student import Student
from account import Account

import dataset


def login():
    username = input("输入用户名:")
    password = input("输入密码:")
    return dataset.verify(username, password)


if __name__ == "__main__":
    dataset.init()
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




