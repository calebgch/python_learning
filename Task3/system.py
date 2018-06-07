from database import Database
from account import Account
from admin import Admin
from teacher import Teacher
from student import Student
import getpass


class System(object):
    def __init__(self):
        self.is_login = False
        self.is_quit = False
        self.db = Database()
        self.user = None

    def run(self):
        while not self.is_quit:
            if not self.is_login:
                self.login()
            else:
                self.do_command()

    def is_quit(self):
        return False

    def login(self):
        username = input("输入用户名:")
        password = getpass.getpass("输入密码:")
        data = self.db.get_one("select * from account where username=\'"+username+"\' and password=\'"+password+"\'")
        if data is None:
            self.is_login = False
        else:
            self.is_login = True
            self.user = self.create_account(data[0], data[1], data[2])
        return self.is_login

    def do_command(self):
        command = input(">>")
        command = command.strip()
        if len(command) != 0:
            if command == 'quit':
                self.quit()
            elif command == 'su':
                self.su()
            else:
                f = getattr(self.user, self.user.command_dict.get(command, ""), None)
                if f is None:
                    print("输入错误，请重新输入")
                else:
                    f()

    def su(self):
        self.is_login = False

    def quit(self):
        print("quit is called.")  
        self.is_quit = True

    def create_account(self, username, password, type):
        if type == 'A':
            return Admin(username, password, type)
        elif type == 'T':
            return Teacher(username, password, type)
        elif type == 'S':
            return Student(username, password, type)
        else:
            return None
