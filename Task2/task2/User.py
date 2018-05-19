class User(object):

    def __init__(self, username, password):
        self.username = "a"
        self.password = "b"
        self.is_login = False
        self.set_username_and_password(username, password)

    def login(self):
        if self.is_login:
            return True
        if self.username == self.password:
            self.is_login = True
        else:
            self.is_login = False
        return self.is_login

    def set_username_and_password(self, username, password):
        self.username = username
        self.password = password
        self.is_login = self.login()



