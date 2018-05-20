import data

class Account(object):

    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type


    def set_username_and_password(self, username, password):
        self.username = username
        self.password = password
        self.is_login = self.login()





