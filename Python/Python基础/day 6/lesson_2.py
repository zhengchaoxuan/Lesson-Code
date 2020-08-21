"""
lesson1：含有默认值的参数

Version : 0.1
Author  : 郑超轩
Date    : 2020/01/22
"""

from random import randint

#含有默认值的参数
def roll_dice(n=2):
    "摇色子"
    total = 0
    for _ in range(n):
        total +=randint(1,6)
    return total

def adds(a=0,b=0,c=0):
    """三个数相加"""
    return a + b + c

print(roll_dice())

#摇三个色子
print(roll_dice(3))

print(adds())
print(adds(1))
print(adds(1,2))
# 传递参数时可以不按照设定的顺序进行传递
print(adds(a=12,c=12))

print('\n\n\n')


"""
lesson2:可变参数

Version : 0.1
Author  : 郑超轩
Date   : 2020/01/22
"""

#在参数名前面的*表示args 是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

#调用add函数
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(1,2,3))
print(add(1,3,5,3))

print('\n\n\n')


"""
lesson3:使用模块进行管理函数

Version : 0.1
Author  : 郑超轩
Date   : 2020/01/22
"""

def foo():
    print('hello,world!')


def foo():
    print('goodbye！')

#调用函数，输出为goodbye!预测其直接把第一个函数给覆盖掉了
foo()

