# 该代码是python从入门到实践的练习源码
# date ：2020/07/19
# version :0.1
# including:
# 1.字典格式：键-值，表示-大括号，动态结构可以直接添加，修改，删除使用del函数
# 2. 如何访问字典，并且知道Python只关心键-值的关联，并不关心键-值的排列顺序，所以输出会出现不是顺序输出，但是可以使用sorted函数进行按照字母排序
# 3.使用for循环进行遍历，例如---for key,value in dictionary.items(): items返回一个键-值对应的列表
# alien = {'color':'red','points':5}
# print(alien.items()) ----->dict_items([('color', 'red'), ('points', 5)])
# 4.使用keys函数可以返回键的列表（遍历字典时，会默认遍历所以的键），使用values函数可以返回值的列表
# 5.set函数---保持元素独一无二的列表（删除重复的元素）
# 6.字典的嵌套：字典列表，列表字典，字典字典
# 7.a = {'a':'A','b':'B'}  c = a.get('c',0)  print(c) 输出0 使用get可判断键是否在字典上面


#练习
alien = {'color':'red','points':5}
print(alien['color'])

alien['x_position'] = 255 #字典是动态结构，所以可以直接添加
alien['y_position'] = 128
print(alien)

alien['color'] ='green'  #字典可以直接修改
print(alien)
print('\n')

alien = {"x_position":0,"y_position":0,'speed':'medium'}    #对外星人进行不同速度的位置追踪
if 'min' == alien['speed']:
    x_increment = 1
elif 'medium' == alien['speed']:
    x_increment = 2
elif 'max'== alien['speed']:
    x_increment = 3

alien['x_position'] = alien['x_position']+x_increment
print(alien['x_position'])
print('\n')

#字典列表---一个元素是字典的列表
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','speed':'max'}
    aliens.append(new_alien)
print(aliens)
print('\n')

# 列表字典---字典的值是列表
favorite_language = {
    'jen': ['python','c'],
    'sarah': ['c','Java'],
    'edward': ['ruby','Matlab'],
    'phil': ['python'] #加括号不然会出现把字符串的一个个字符当作列表输出
    }
for name,languages in favorite_language.items():
    print('\n'+name+' favorite languages are:')
    for language in languages:
        print(language)
print('\n')

#字典字典--字典中包含另一个字典

#6-1 人
user = {
     'surname':'zheng',
     'name':'chaoxuan',
     'age':21,
     'city':'daozou'
     }
print(user['surname'])
print(user['name'])
print(user['age'])
print(user['city'])
print('\n')

# 6-2 喜欢的数字
favorite_number = {
    'zcx':12,
    'wqd':24,
    'pyy':36,
    'zzy':48,
    'wz':60
    }
print('zcx favorite number is '+ str(favorite_number['zcx']))
print('wqd favorite number is '+ str(favorite_number['wqd']))
print('pyy favorite number is '+ str(favorite_number['pyy']))
print('zzy favorite number is '+ str(favorite_number['zzy']))
print('wz favorite number  is '+ str(favorite_number['wz']))
print('\n')

#6-3
vocabulary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
print('string: '+vocabulary['string'])
print('comment: '+vocabulary['comment'])
print('list: '+vocabulary['list'])
print('loop: '+vocabulary['loop'])
print('dictionary: '+vocabulary['dictionary'])
print('\n')

#6-4 改进6-3
for key,value in vocabulary.items(): #使用items函数进行循环操作
    print(key+' : '+value)
print('\n')

#6-5 河流
rivers = {
    'nile':'egypt',
    'changjian':'china',
    'laiying':'russia',
    'liluo':'yamaxun'
    }
for key,value in rivers.items():
    print(f'The {key.title()} runs through {value.title()}.')  #循环为每条河流打印一条消息

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)
print('\n')

#6-6 调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for key in favorite_languages.keys():
    if key in coders:
        print('Thank you for taking the poll '+key.title()+' !')
    else:
        print('I hope you can have time to take the poll'+key.title()+' !')
print('\n')

#6-7 人 -- 字典列表
user1 = {
         'surname':'wang',
     'name':'mengting',
     'age':21,
     'city':'heping'
    }
user2 = {
         'surname':'peng',
     'name':'yulong',
     'age':21,
     'city':'heping'
    }
user3 = {
     'surname':'zheng',
     'name':'chaoxuan',
     'age':21,
     'city':'daozou'
     }
users = [user1,user2,user3]
for user in users:
    print(user)

#6-9 喜欢的地方 --- 列表字典
favorite_places ={
    'zcx':['biejin','shanghai','congqing'],
    'wqd':['shengyang','biejing'],
    'cjl':['lasha'],
    }
for name,places in favorite_places.items():
    print('\n'+name+' favorite place are :')
    for place in places:
        print(place)

# 城市
citys = {
    'Beijin':{
        'country':'china',
        'population':1500000,
        'fact':'the capital of china'
        },
    'NewYork':{
        'country':'america',
        'population':1800000,
        'fact':'the financial center of world'
        },
    'shanghai':{
        'country':'china',
        'population':1400000,
        'fact':'the financial center of china'
        }
    }
for city,messages in citys.items():
    print('\n'+'welcome to the '+city)
    for key,value in messages.items():
        print(key+' : '+str(value))


