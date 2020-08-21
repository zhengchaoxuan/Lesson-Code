# 该代码是python从入门到实践的练习源码
# date ：2020/07/19
# version :0.1
# date ：2020/07/20
# version :0.2
# including:
# 1.实参和形参，传递参数的方式--（位置参数和关键字传递），形参可以添加默认值（只能在后面的参数），可变参数（*）--组成空的列表，（**）--字典
# 2.传递列表，列表在传递给函数后，可直接在函数中进行修改，并且函数对于列表的所做的任何修改都是永久性的
# 3.程序有一个理念---即每个函数都只复制一个功能
# 4.如何禁止函数修改列表 --- 把列表的副本传递给函数，即实参使用list[:]--除非有足够的理由进行复制否则不用因为函数的复制等会花费时间
# 5.可变参数和字典的结合
# 6.了解import，模块，函数，以及关键字as(别名)，使用from time import * 代表导入模块的所有函数
# 7.Python可能遇到多个名称相同的函数和变量，它选择的方式是覆盖函数，而不是分别导入
# 8.规范：形参和实参进行关键字传递时等号两边不要空行


# 8-3 默认参数，传递参数（关键字，位置），变长参数--def 函数名（*参数）--创建一个空的元组：
def make_shirt(size,stype='I love Python'):
    print('the T-shirt size is '+size)
    print('and its stype is '+stype)

make_shirt('xxL','popular')
make_shirt('xL')
print('\n')

# 8-6 城市名
def city_country(city,country):
    message =city+' , '+country
    return message.title()

print(city_country('santiago','chile'))
print(city_country('shanghai','china'))
print('\n')

#8-7 专辑
def make_album(name,album,album_number = 12):
    album_message ={
        'name':name,
        'album':album,
        'album_number': album_number
    }
    return album_message

print(make_album('taylor','red',23))
print(make_album('Avril','above water'))
print(make_album('Adele','hello',15))

# 8-8 用户专辑
albums_list =[]
while True:
    name = input('enter singer :')
    album = input('his(her) album: ')
    album_number = int(input('his(her) album_number: '))
    albums_list.append(make_album(name,album,album_number))
    repeat = input('would you want to enter(yes/no): ')
    if repeat =='yes':
        continue
    if repeat == 'no':
        break
    if repeat!='yes' or repeat!='no':
        repeat = input('enter error,would you want to enter(yes/no): ')
    
print(albums_list)

# date ：2020/07/20
# version :0.1

#  练习 --- 在列表传递给函数后，函数对列表所做的任何修改都是永久的(列表局部修改赋值，而不是之间进行赋值)
def a(names):
    names[1] = 23

use_name = ['a','b','c']
a(use_name)
print(use_name)

# 8-9 魔术师(显示)
def show_magicians(names):
    for name in names:
        print(name)

magician_name = ['zcx','wz','wqd']
show_magicians(magician_name)

# 8-10 修改加显示魔法师
# 第一种方法
def make_great(names):
    for i in range(len(names)):
        names[i] = 'the great '+names[i]
# 书上的方法
def make_great1(names):
    new_names=[]
    while names:
        name = names.pop(0)
        new_name ='the great '+ name
        new_names.append(new_name)

    for new_name in new_names:
        names.append(new_name)

def show_magician(names):
    for name in names:
        print(name)

magician_name = ['zcx','wz','wqd']
make_great1(magician_name)
show_magician(magician_name)
print('\n')

# 8-11 不变的魔法师
def make_greats(names):
        for i in range(len(names)):
            names[i] = 'the great '+names[i]
        return names
magician_name = ['zcx','wz','wqd']
magician_names = []
magician_names = make_greats(magician_name[:])
show_magicians(magician_name)
show_magicians(magician_names)
print('\n')

# 8-12 sandwich  ---延长实参
def add_sandwish(*food):
    print('the sandwich is delicious!')

add_sandwish('apple','banana')
add_sandwish('apple','banana','a')
print('\n') 

#8-13 用户简介 -- 字典和关键字和延长函数
def build_profile(supname,name,**messages):
    introduction = {}
    introduction['supname'] = supname
    introduction['name'] = name
    for key,value in messages.items():
        introduction[key] = value
    return introduction

user_profile =build_profile('zheng','chaoxuan',age=12,sex = 'boy')
print(user_profile)









