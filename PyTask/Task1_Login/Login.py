#用户输入用户名密码，验证通过后输出"输入正确，进入程序"，不通过输出："用户名密码输入错误，请重新输入"
#同一用户3次输入错误，进行锁定。如果是被锁定用户，输出："您是被锁定用户，请联系管理员"
#用户名密码保存在文件中
#输出登录操作记录

#with用法可以把open/close组在一起成对出现
#join转字符串的方法还可以改改

#用户名密码信息
user_dict = {}
#用户登录失败信息
failed_record = {}


#读取加载account.txt文件
def load_account():
    p = open('./account.txt', 'r', encoding='UTF-8')
    for line in p.readlines():
        if line.startswith('#'):
            continue
        account = line.split(',')
        if len(account) == 1:
            continue
        user = account[0].split()[0]
        password = account[1].split()[0]
        user_dict[user] = password
        failed_record[user] = 0
    p.close()


#输入用户名密码
def input_info():
    username = input('please enter your name: ')
    password = input('please enter your password: ')
    return [username, password]

#判断是否为锁定用户
def is_locked(account):
    info = failed_record.get(account[0])
    if info == None:
        return False
    elif failed_record[account[0]] == 3:
        return True
    else:
        return False

#登录操作后的处理
def do_login(username, result):
    if result:
        failed_record[username] = 0
    else:
        tmp = failed_record.get(username)
        if tmp != None:
            failed_record[username] += 1


def login():
    account = input_info()
    if is_locked(account):
        print("您是被锁定用户，请联系管理员")
        return 2
    if verify(account) == True:
        print("输入正确，进入程序")
        do_login(account[0], True)
        return 0
    else:
        print("用户名密码输入错误，请重新输入")
        do_login(account[0], False)
        return 1


def verify(account):
    password = user_dict.get(account[0])
    if password != None and account[1] == password:
        return True
    else:
        return False


#显示当前保存的信息
def show():
    print("user list:")
    show_users()
    print("failed records:")
    show_failed_record()

def show_users():
    for k,v in user_dict.items():
        print("\tuser:"+k+", password:"+v)

def show_failed_record():
    for k,v in failed_record.items():
        print("\tuser:"+k+", failedtimes:"+str(v))


if __name__ == "__main__":
    load_account()
    #show()
    result = 1
    while result != 0:
        result = login()
    #show()
