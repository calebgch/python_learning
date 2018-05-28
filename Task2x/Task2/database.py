import pickle
import os


user_list = []
school_list = []
course_list = []
score_list = []


def save(data_list):
    if len(data_list) != 4:
        print("invalid parameter")
        return
    user_list = data_list[0]
    school_list = data_list[1]
    course_list = data_list[2]
    score_list = data_list[3]
    with open('./dump/data.pk', 'wb') as f:
        pickle.dump([user_list, school_list, course_list, score_list], f)


def load():
    with open('./dump/data.pk', 'rb') as f:
        data_list = pickle.load(f)
        global user_list
        user_list = data_list[0]
        global school_list
        school_list = data_list[1]
        global course_list
        course_list = data_list[2]
        global score_list
        score_list = data_list[3]


def get():
    load()
    return [user_list, school_list, course_list, score_list]


def init():
    if not os.path.exists('./dump/data.pk'):
        data_list = [[], [], [], []]
        save(data_list)

