from account import Account
import getpass
from database import Database
from prettytable import PrettyTable


class Admin(Account):
    """docstring for Admin"""
    def __init__(self, username, password, type):
        super().__init__(username, password, type)
        self.command_dict['add user'] = 'add_user'
        self.command_dict['del user'] = 'del_user'
        self.command_dict['show user'] = 'show_user'
        self.command_dict['add school'] = 'add_school'
        self.command_dict['del school'] = 'del_school'
        self.command_dict['show school'] = 'show_school'
        self.command_dict['add course'] = 'add_course'
        self.command_dict['del course'] = 'del_course'
        self.command_dict['show course'] = 'show_course'

    def help(self):
        for key in self.command_dict.keys():
            print(key)

    def add_school(self, school_name, school_addr):
        if self.is_school_exist():
            print("学校已存在")
        else:
            pass

    def is_school_exist(self, school_name):
        sql = "select * from school where school_name='%(school_name)s'"%{'school_name':school_name}
        db = Database()
        school = db.get_one(sql)
        if school is None:
            return False
        else:
            return True

    def is_user_exist(self, username):
        sql = "select * from account where username='%s'"%(username)
        db = Database()
        account = db.get_one(sql)
        if account is None:
            return False
        else:
            return True

    def add_user(self):
        new_username = input("输入新用户名：")
        new_password = getpass.getpass("输入密码：")
        new_password2 = getpass.getpass("再次输入密码：")
        new_type = input("输入用户类型：")

        if self.is_user_exist(new_username):
            print("用户名称已存在，新建用户失败")
            return

        if new_password != new_password2:
            print("密码不一致，新建用户失败")
            return

        sql = "insert into account (username, password, type) values ('%(username)s', '%(password)s', '%(type)s')"%{'username':new_username, 'password':new_password, 'type':new_type}
        db = Database()
        db.execute(sql)

    def del_user(self):
        username = input("输入需要删除的用户名：")
        sql = "delete from account where username='%(username)s'"%{'username':username}
        db = Database()
        db.execute(sql)

    def show_user(self):
        sql = "select * from account"
        db = Database()
        accounts = db.get_all(sql)
        x = PrettyTable(["用户名", "用户密码", "用户类型"])
        for account in accounts:
            x.add_row([account[0], account[1], account[2]])
        print(x)

    def create_account(self, username, password, type):
        if type == 'A':
            return Admin(username, password, type)
        elif type == 'T':
            return Teacher(username, password, type)
        elif type == 'S':
            return Student(username, password, type)
        else:
            return None
