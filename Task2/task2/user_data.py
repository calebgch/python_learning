import data
from account import Account


class UserData(object):
    user_list = []

    def __init__(self):
        if len(self.user_list) == 0:
            self.user_list = data.load('user')

    def login(self, username, password):
        for account in self.user_list:
            if account.username == username and account.password == password:
                return account
        return None

    def add_account(self, username, password, type):
        if self.account_in_list(username):
            return False
        account = Account(username, password, type)
        self.add_account(account)

    def add_account(self, account):
        self.user_list.append(account)
        data.save('user', self.user_list)

    def account_in_list(self, username):
        for account in self.user_list:
            if account.username == username:
                return True
        return False