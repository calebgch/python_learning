import pickle


def to_file(flag):
    if flag == 'user':
        return './dump/account.pk'
    elif flag == '':
        return './dump/data.pk'


def save(flag, object):
    filepath = to_file(flag)
    with open(filepath, 'wb') as f:
        pickle.dump(object, f)


def load(flag):
    with open(to_file(flag), 'rb') as f:
        return pickle.load(f)
