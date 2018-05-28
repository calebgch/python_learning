import database
from school import School


class Account(object):
    def __init__(self, username, password, type):
        self.username = username
        self.passowrd = password
        self.type = type

    def help(self):
        pass

    def do_command(self, command):
        pass


class Admin(Account):
    def __init__(self, username, password):
        super().__init__(username, password, 'A')

    def help(self):
        print('add user #添加用户\n'
              'del user #删除用户\n'
              'add school #添加学校\n'
              'del school #删除学校\n'
              'add course #添加课程\n'
              'del course #删除课程\n'
              'add teacher #添加老师\n'
              'del teacher #删除老师\n'
              'show user #显示用户')

    def do_command(self, command):
        if command == 'add user':
            self.add_user()
        elif command == 'del user':
            self.del_user()
        elif command == 'add school':
            self.add_school()
        elif command == 'del school':
            self.del_school()
        elif command == 'show school':
            self.show_school()
        elif command == 'add course':
            pass
        elif command == 'del course':
            pass
        elif command == 'add teacher':
            pass
        elif command == 'del teacher':
            pass
        elif command == 'show user':
            self.show_user()

    def add_user(self):
        new_username = input("输入新用户名:")
        new_password = input("输入密码:")
        new_type = input("输入用户类型:")
        account = self.create_account(new_username, new_password, new_type)
        datalist = database.get()
        datalist[0].append(account)
        database.save(datalist)

    def del_user(self):
        username = input("输入要删除的用户名:")
        datalist = database.get()
        user_list = datalist[0]
        for account in user_list:
            if account.username == username:
                user_list.remove(account)
                print('用户删除成功')
                database.save(datalist)
                return True
        print('用户删除失败')
        return False

    def create_account(self, username, password, type):
        if type == 'Admin' or type == 'A':
            return Admin(username, password)
        elif type == 'Teacher' or type == 'T':
            return Teacher(username, password)
        elif type == 'Studeng' or type == 'S':
            return #Student(username, password)
        else:
            return None

    def add_school(self):
        school_name = input("输入学校名:")
        school_addr = input("输入学校地址:")
        new_school = School(school_name, school_addr)
        datalist = database.get()
        school_list = datalist[3]
        for school in school_list:
            if school.name == new_school.name:
                print("新增学校失败，学校已存在")
                return
        school_list.append(new_school)
        database.save(datalist)

    def del_school(self):
        school_name = input("输入需要删除的学校名:")
        datalist = database.get()
        school_list = datalist[3]
        for school in school_list:
            if school.name == school_name:
                school_list.remove(school)
                database.save(datalist)
                print("学校删除成功")
                return
        print('学校删除失败，未找到学校')

    def show_school(self):
        datalist = database.get()
        school_list = datalist[3]
        for school in school_list:
            print(school.name, school.addr)

    def show_user(self):
        datalist = database.get()
        user_list = datalist[0]
        for account in user_list:
            print(account.username, account.passowrd, account.type)

    def add_teacher(self):
        pass
    def del_teacher(self):
        pass
    def show_teacher(self):
        pass

class Teacher(Account):
    def __init__(self, username, password):
        super().__init__(username, password, 'T')

    def help(self):
        print('show course #查看教授课程\n'
              'show student #查看学生\n'
              'show score #查看学生成绩\n')

    def do_command(self, command):
        if command == 'show course':
            pass
        elif command == 'show student':
            pass
        elif command == 'show score':
            pass
        elif command == 'set score':
            pass


class Student(Account):

    def __init__(self, username, password):
        super().__init__(username, password, 'S')

    def register_class(self):
        pass

    def get_courses(self):
        pass

    def do_command(self, command):
        if command == 'register course':
            pass
        elif command == 'quit course':
            pass
        elif command == 'show course':
            pass

    def help(self):
        print('register course #报名课程\n'
              'quit course #退出课程\n'
              'show course #显示已报名课程')



