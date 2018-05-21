import pickle
from account import Account

class Data(object):
    user_list = []
    school_list = []
    teacher_list = []
    student_list = []
    course_list = []
    score_list = []

    def __init__(self):
        if len(self.user_list) == 0:
            self.user_list = self.load('user')

    def login(self, username, password):
        for account in self.user_list:
            if account.username == username and account.password == password:
                return account
        return None

    def add_account(self, username, password, type):
        if self.account_in_list(username):
            print("Error：用户名已注册。")
            return False
        if type != 'Admin' and type != 'Teacher' and type != 'Student':
            print("Error：用户类型错误")
            return False
        return True

    def add_account2(self, account):
        self.user_list.append(account)
        self.save('user', self.user_list)

    def del_account(self, username):
        if not self.account_in_list(username):
            print('Error：用户名不存在')
            return False
        for account in self.user_list:
            if account.username == username:
                self.user_list.remove(account)
                return True
        return False

    def account_in_list(self, username):
        for account in self.user_list:
            if account.username == username:
                return True
        return False

    def to_file(self, flag):
        if flag == 'user':
            return './dump/account.pk'
        elif flag == '':
            return './dump/data.pk'

    def save(self, flag, obj):
        with open(self.to_file(flag), 'wb') as f:
            pickle.dump(obj, f)

    def load(self, flag):
        with open(self.to_file(flag), 'rb') as f:
            return pickle.load(f)
