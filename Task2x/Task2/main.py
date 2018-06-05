import database
from account import Account
from account import Admin


def init():
    database.init()


def login():
    username = input("输入用户名:")
    password = input("输入密码:")
    data_list = database.get()
    user_list = data_list[0]
    for account in user_list:
        if account.username == username and account.passowrd == password:
            return account
    return None


def main():
    data_list = database.get()
    user_list = data_list[0]
    if len(user_list) == 0:
        account = Admin('admin', 'admin')
        user_list.append(account)
    data_list[0] = user_list
    database.savedata(data_list)

    account = login()
    while account is None:
        account = login()
    print("成功登录")
    command = ""
    while command != "quit" and command != "exit":
        command = input(">>")
        if command == 'help':
            account.help()
        elif command == 'su':
            account = login()
        else:
            account.do_command(command)
    print("exit system")


if __name__ == "__main__":
    init()
    main()

