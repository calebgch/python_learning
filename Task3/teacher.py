from account import Account
from database import Database
from prettytable import PrettyTable


class Teacher(Account):
    """docstring for Teacher"""
    def __init__(self, username, password, type):
        super().__init__(username, password, type)
        # command name : function name
        self.command_dict['set score'] = 'set_score',
        self.command_dict['show score'] = 'show_student',
        self.command_dict['show student'] = 'show_student',
        self.command_dict['show course'] = 'show_course',
        self.command_dict['show school'] = 'show_school'

    def help(self):
        for key in self.command_dict.keys():
            print(key)

    def show_course(self):
        sql = "select * from course"
        db = Database()
        courses = db.get_all(sql)
        x = PrettyTable(["课程名称", "课程老师", "所属学校"])
        for course in courses:
            if course[2] == self.username:
                x.add_row([course[0], course[1], course[2]])
        print(x)

    def show_student(self):
        sql = "select * from score where teacher='%(teacher_name)s'"%{'teacher_name':self.username}
        db = Database()
        students = db.get_all(sql)

        x = PrettyTable(["学生名字", "课程名称", "分数", "任课老师"])
        for student in students:
            x.add_row([score[1], course[0], score[2], course[3]])
        print(x)

    def set_score(self):
        course_name = input("输入要修改的课程:")
        student_name = input("输入要修改的学生:")
        new_score = input("分数:")
        sql = "update score set score=%(score)d where course_name='%(course_name)s' and student_name='%(student_name)s'"%{'score':new_score, 'course_name':course_name, 'student_name':student_name}
        db = Database()
        db.excute(sql)

    def show_school(self):
        sql = "select * from school"
        db = Database()
        schools = db.get_all(sql)

        x = PrettyTable(["学校名称", "学校地址"])
        for school in schools:
            x.add_row([school[0], school[1]])
        print(x)


