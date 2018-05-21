import pickle
from account import Account



class Data(object):
    user_list = []
    teacher_list = []
    student_list = []
    school_list = []
    course_list = []
    score_list = []

    def __init__(self):
        if len(self.user_list) == 0:
            self.user_list = self.load('user')
            data_list = self.load('data')
            self.school_list = data_list[0]
            self.course_list = data_list[1]
            self.score_list = data_list[2]

    def login(self, username, password):
        for account in self.user_list:
            if account.username == username and account.password == password:
                return account
        return None

    def add_account(self, account):
        self.user_list.append(account)
        self.save('user', self.user_list)

    def del_account(self, username):
        for account in self.user_list:
            if account.username == username:
                self.user_list.remove(account)
                self.save('user', self.user_list)
                return True
        print('Error：用户名不存在')
        return False

    def show_account(self):
        for account in self.user_list:
            print(account.username, account.password, account.type)

    def account_in_list(self, username):
        for account in self.user_list:
            if account.username == username:
                return True
        return False

    def to_file(self, flag):
        if flag == 'user':
            return './dump/account.pk'
        elif flag == 'data':
            return './dump/data.pk'

    def save(self, flag, obj):
        with open(self.to_file(flag), 'wb') as f:
            pickle.dump(obj, f)

    def load(self, flag):
        with open(self.to_file(flag), 'rb') as f:
            return pickle.load(f)
