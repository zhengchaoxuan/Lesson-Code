# 该代码是python从入门到实践的练习源码
# date ：2020/07/21
# version : 0.1

import json
'''10-11,12 喜欢的数字'''
while True:
    try:
        file_name = 'Python从入门到实践/10文件处理/like_number.json'
        with open(file_name,'r') as  file_object:
            like_number = json.load(file_object)
        print('I know your favorite number! It is '+str(like_number))
        break
    except FileNotFoundError:
        number = input('input you like number: ')
        number = int(number)
        with open(file_name,'w') as file_object:
            json.dump(number,file_object)


'''10-13 验证用户'''
def greet_user(name):
    file_name = 'Python从入门到实践/10文件处理/name.json'
    names = 'zhengchaoxuan'
    with open(file_name,'w') as file_object:
        json.dump(names,file_object)

    try:
        with open(file_name) as file_object:
            user_name = json.load(file_object)
            while True:
                if(name == user_name):
                    print('welcome '+str(name))
                    break
                else:
                    name = get_new_username()
    except FileNotFoundError:
        print('can not find the file!')

def get_new_username():
    username  = input('name error! enter the right name: ')
    return username

user_name = input('enter your name: ')
greet_user(user_name)
