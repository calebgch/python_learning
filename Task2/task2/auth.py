import data


class Auth(object):
    def __init__(self):
        self.user_list = data.load('user')

    def login(self, username, password):
        for account in self.user_list:
            if account.username == username and account.password == password:
                return account
        return None





def load():
    account = data.load('user')
    return account


def save(account):
    data.save('user', account)


def modify(account, new_user, new_pass):
    account.set_username_and_password(new_user, new_pass)
    return account

