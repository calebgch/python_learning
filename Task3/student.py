from account import Account
from database import Database
from prettytable import PrettyTable


class Student(Account):
    """docstring for Student"""
    def __init__(self, username, password, type):
        super().__init__(username, password, type)
        self.command_dict['register course'] = 'register_course'
        self.command_dict['show course'] = 'show_course'
        self.command_dict['quit course'] = 'quit_course'

    def help(self):
        for key in self.command_dict.keys():
            print(key)

    def register_course(self):
        course_name = input("输入要报名的课程:")
        school_name = input("输入课程所在学校:")
        if not self.is_course_exist(school_name, course_name):
            print('报名失败，课程不存在')
            return
        sql = "insert into score (school_name, course_name, student_name, score) values ('%s', '%s', '%s', 0)"%(school_name, course_name, self.username)
        db = Database()
        db.execute(sql)

    def is_course_exist(self, school_name, course_name):
        sql = "select * from course where school_name='%s' and course_name='%s'"%(school_name, course_name)
        db = Database()
        course = db.get_one(sql)
        if course is None:
            return False
        else:
            return True

    def show_course(self):
        sql = "select * from score where student_name = '%s'"%(self.username)
        db = Database()
        scores = db.get_all(sql)
        x = PrettyTable(["课程名称", "所属学校", "课程分数", "学生名字"])
        for score in scores:
            x.add_row([score[0], score[1], score[2], score[3]])
        print(x)

    def quit_course(self):
        course_name = input("输入要退出的课程:")
        school_name = input("输入课程所在学校:")
        if not self.is_course_exist(school_name, course_name):
            print('退出失败，课程不存在')
            return

        sql = "delete from score where student_name='%s' and course_name='%s' and school_name='%s'"%(self.username, course_name, school_name)
        db = Database()
        db.execute(sql)
