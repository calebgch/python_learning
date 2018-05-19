from User import User


if __name__ == "__main__":
    command = ""
    user = User("a", "b")
    while command != "quit" or command != "exit":
        if not user.login():
            username = input("username:")
            password = input("password:")
            user.set_username_and_password(username, password)
            continue
        print("login...")
        command = input(">>")
        print("command"+command)


