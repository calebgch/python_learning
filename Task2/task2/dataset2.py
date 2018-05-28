import pickle
import admin
import student
import teacher
import account

data_list = []
user_list = []
school_list = []


def init():
    admin = Admin('admin', 'passw0rd')
    global user_list
    user_list = [admin]
    with open('data.pk', 'wb') as f:
        pickle.dump([user_list, data_list], f)


def show():
    pass


def save():
    with open('data.pk', 'wb') as f:
        pickle.dump([user_list, data_list], f)


def load():
    with open('data.pk', 'rb') as f:
        all_list = pickle.load(f)
    global user_list
    global data_list
    user_list = all_list[0]
    data_list = all_list[1]



