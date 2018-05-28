import database
from school import School
from course import Course


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
            self.add_course()
        elif command == 'del course':
            self.del_course()
        elif command == 'show course':
            self.show_course()
        elif command == 'show teacher':
            self.show_teacher()
        elif command == 'show student':
            self.show_student()
        elif command == 'show user':
            self.show_user()

    def add_user(self):
        new_username = input("输入新用户名:")
        new_password = input("输入密码:")
        new_type = input("输入用户类型:")
        account = self.create_account(new_username, new_password, new_type)
        if account is not None and self.verify_user(account):
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
            school = input("输入老师所属学校:")
            return Teacher(username, password, school)
        elif type == 'Student' or type == 'S':
            school = input("输入学生所属学校:")
            return Student(username, password, school)
        else:
            return None

    def verify_user(self, verify_user):
        datalist = database.get()
        user_list = datalist[0]
        for account in user_list:
            if account.username == verify_user.username:
                print('用户验证失败，存在同名用户')
                return False
        return True

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

    def show_teacher(self):
        datalist = database.get()
        user_list = datalist[0]
        for account in user_list:
            if account.type == 'T':
                print(account.username, account.passowrd, account.type)

    def show_student(self):
        datalist = database.get()
        user_list = datalist[0]
        for account in user_list:
            if account.type == 'S':
                print(account.username, account.passowrd, account.type)

    def add_course(self):
        course_name = input("输入课程名:")
        course_school = input("输入开课学校:")
        course_teacher = input("输入任课教师:")
        course = self.create_course(course_name, course_school, course_teacher)
        if course is not None:
            datalist = database.get()
            course_list = datalist[2]
            course_list.append(course)
            database.save(datalist)

    def create_course(self, course_name, course_school, course_teacher):
        datalist = database.get()
        user_list = datalist[0]
        course_list = datalist[2]
        for course in course_list:
            if course.name == course_name and course.school == course_school:
                print("新增课程失败，课程已存在")
                return None
        for account in user_list:
            if account.username == course_teacher:
                return Course(course_name, course_school, course_teacher)
        print("新增课程失败，指定的教师不存在")
        return None

    def del_course(self):
        course_name = input("输入要删除的课程名:")
        course_school = input("输入课程所在学校:")
        datalist = database.get()
        course_list = datalist[2]
        for course in course_list:
            if course.name == course_name and course.school == course_school:
                print("新增课程失败，课程已存在")
                return None

    def show_course(self):
        datalist = database.get()
        course_list = datalist[2]
        for course in course_list:
            print(course.name, course.school, course.teacher)


class Teacher(Account):
    def __init__(self, username, password, school):
        self.school = school
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

    def show_course(self):
        datalist = database.get()
        course_list = datalist[2]
        for course in course_list:
            if course.teacher == self.username:
                print(course.name, course.school, course.teacher)

 
class Student(Account):

    def __init__(self, username, password, school):
        self.school = school
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



