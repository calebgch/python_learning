
class Account(object):
    def __init__(self, username, password, type):
        self.username = username
        self.passowrd = password
        self.type = type
        self.command_dict = {"help": "help"}

    def help(self):
        pass

    def do_command(self, command):
        pass
