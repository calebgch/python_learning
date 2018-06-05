from database import Database


class System(object):
    def __init__(self):
        self.is_login = False
        self.is_quit = False
        self.db = Database()

    def run(self):
        while not self.is_quit:
            if not self.is_login:
                self.login()

    def is_quit(self):
        return False

    def login(self):
        username = input("输入用户名:")
        password = input("输入密码:")
        data = self.db.get_one("select * from account where username=\'"+username+"\' and password=\'"+password+"\'")
        if data is None:
            self.is_login = False
        else:
            self.is_login = True
        return self.is_login
