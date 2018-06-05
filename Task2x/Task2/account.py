import database
from school import School
from course import Course
from prettytable import PrettyTable


def get_user_list():
    datalist = database.get()
    return datalist[0]


def get_school_list():
    datalist = database.get()
    return datalist[1]


def get_course_list():
    datalist = database.get()
    return datalist[2]


def get_score_list():
    datalist = database.get()
    return datalist[3]


def save():
    database.save()


def user_exist(username):
    user_list = get_user_list()
    for account in user_list:
        if account.username == username:
            return True
    return False


def school_exist(school_name):
    school_list = get_school_list()
    for school in school_list:
        if school.name == school_name:
            return True
    return False


def course_exist(course_name, schoolname):
    course_list = get_course_list()
    for course in course_list:
        if course.name == course_name and course.school == schoolname:
            return True
    return False


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
              'show user #显示用户\n'
              'show teacher #显示老师\n'
              'show student #显示学生\n'        
              'add school #添加学校\n'
              'del school #删除学校\n'
              'show school #显示学校\n'
              'add course #添加课程\n'
              'del course #删除课程\n'
              'show course #显示课程\n')

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
        if account is not None:
            user_list = get_user_list()
            user_list.append(account)
            save()

    def del_user(self):
        username = input("输入要删除的用户名:")
        user_list = get_user_list()
        for account in user_list:
            if account.username == username:
                user_list.remove(account)
                print('用户删除成功')
                save()
                return True
        print('用户删除失败')
        return False

    def create_account(self, username, password, type):
        if user_exist(username):
            print('用户创建失败：用户名已存在')
            return None
        if type == 'Admin' or type == 'A':
            return Admin(username, password)
        elif type == 'Teacher' or type == 'T':
            school = input("输入老师所属学校:")
            if school_exist(school):
                return Teacher(username, password, school)
        elif type == 'Student' or type == 'S':
            school = input("输入学生所属学校:")
            if school_exist(school):
                return Student(username, password, school)
        else:
            return None

    def add_school(self):
        school_name = input("输入学校名:")
        school_addr = input("输入学校地址:")
        new_school = School(school_name, school_addr)
        school_list = get_school_list()
        for school in school_list:
            if school.name == new_school.name:
                print("新增学校失败，学校已存在")
                return
        school_list.append(new_school)
        save()

    def del_school(self):
        school_name = input("输入需要删除的学校名:")
        school_list = get_school_list()
        for school in school_list:
            if school.name == school_name:
                school_list.remove(school)
                save()
                print("学校删除成功")
                return
        print('学校删除失败，未找到学校')

    def show_school(self):
        school_list = get_school_list()
        x = PrettyTable(["学校名称", "学校地址"])
        for school in school_list:
            x.add_row([school.name, school.addr])
        print(x)

    def show_user(self):
        user_list = get_user_list()
        x = PrettyTable(["用户名", "密码", "用户类型"])
        for account in user_list:
            x.add_row([account.username, account.passowrd, account.type])
        print(x)

    def show_teacher(self):
        user_list = get_user_list()
        x = PrettyTable(["老师名字", "密码", "所属学校"])
        for account in user_list:
            if account.type == 'T':
                x.add_row([account.username, account.passowrd, account.school])
        print(x)

    def show_student(self):
        user_list = get_user_list()
        x = PrettyTable(["学生名字", "密码", "所属学校"])
        for account in user_list:
            if account.type == 'S':
                x.add_row([account.username, account.passowrd, account.school])
        print(x)

    def add_course(self):
        course_name = input("输入课程名:")
        course_school = input("输入开课学校:")
        course_teacher = input("输入任课教师:")
        course = self.create_course(course_name, course_school, course_teacher)
        if course is not None:
            course_list = get_course_list()
            course_list.append(course)
            save()

    def create_course(self, course_name, course_school, course_teacher):
        if not user_exist(course_teacher):
            print("新增课程失败，指定的教师不存在")
            return None
        if not school_exist(course_school):
            print("新增课程失败，指定的学校不存在")
            return None
        if course_exist(course_name, course_school):
            print("新增课程失败，课程已存在")
            return None
        return Course(course_name, course_school, course_teacher)

    def del_course(self):
        course_name = input("输入要删除的课程名:")
        course_school = input("输入课程所在学校:")
        course_list = get_course_list()
        for course in course_list:
            if course.name == course_name and course.school == course_school:
                course_list.remove(course)
                save()
                return
        print('课程删除失败，没有找到对应的课程')

    def show_course(self):
        course_list = get_course_list()
        x = PrettyTable(["课程名称", "所属学校", "任课老师"])
        for course in course_list:
            x.add_row([course.name, course.school, course.teacher])
        print(x)


class Teacher(Account):
    def __init__(self, username, password, school):
        self.school = school
        super().__init__(username, password, 'T')

    def help(self):
        print('show course #查看教授课程\n'
              'show student #查看学生\n'
              'show score #查看学生成绩\n'
              'set score #修改学生成绩')

    def do_command(self, command):
        if command == 'show course':
            self.show_course()
        elif command == 'show student':
            self.show_student()
        elif command == 'show score':
            self.show_student()
        elif command == 'set score':
            self.set_score()

    def show_course(self):
        course_list = get_course_list()
        x = PrettyTable(["课程名称", "课程老师", "所属学校"])
        for course in course_list:
            if course.teacher == self.username:
                x.add_row([course.name, course.teacher, course.school])
        print(x)

    def show_student(self):
        course_list = get_course_list()
        score_list = get_score_list()
        x = PrettyTable(["学生名字", "课程名称", "分数", "任课老师"])
        for course in course_list:
            if course.teacher == self.username:
                for score in score_list:
                    if score.course_name == course.name and score.school == course.school:
                        x.add_row([score.student_name, course.name, score.score, course.name])
        print(x)

    def set_score(self):
        course_name = input("输入要修改的课程:")
        student_name = input("输入要修改的学生:")
        new_score = input("分数:")
        score_list = get_score_list()
        for score in score_list:
            if score.course_name == course_name and score.student_name == student_name:
                score.set_score(new_score)
        save()


class Student(Account):
    def __init__(self, username, password, school):
        self.school = school
        super().__init__(username, password, 'S')

    def do_command(self, command):
        if command == 'register course':
            self.register_course()
        elif command == 'quit course':
            self.quit_course()
        elif command == 'show course':
            self.show_course()

    def register_course(self):
        course_name = input("输入要报名的课程:")
        school_name = input("输入课程所在学校:")
        if not course_exist(course_name, school_name):
            print('报名失败，课程不存在')
        score = Score(course_name, school_name, self.username)
        score_list = get_score_list()
        score_list.append(score)
        save()

    def show_course(self):
        score_list = get_score_list()
        x = PrettyTable(["课程名称", "所属学校", "课程分数", "学生名字"])
        for score in score_list:
            if score.student_name == self.username:
                x.add_row([score.course_name, score.school, score.score, score.student_name])
        print(x)

    def quit_course(self):
        course_name = input("输入要退出的课程:")
        school_name = input("输入课程所在学校:")
        if not course_exist(course_name, school_name):
            print('退出失败，课程不存在')
        score_list = get_score_list()
        for score in score_list:
            if score.course_name == course_name and score.school == school_name and score.student_name == self.username:
                score_list.remove(score)
                save()

    def help(self):
        print('register course #报名课程\n'
              'quit course #退出课程\n'
              'show course #显示已报名课程')


class Score(object):
    def __init__(self, course_name, school_name, student_name):
        self.student_name = student_name
        self.course_name = course_name
        self.score = 0
        self.school = school_name

    def set_score(self, score):
        self.score = score


