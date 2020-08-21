"""
exercise:实现判断一个数是不是回文数的函数

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/22
"""

def hws(number):
    sum_old = number
    sums = 0
    while number > 0:
        sums = number%10+sums*10
        number//=10
        
    if sum_old == sums:
        return True
    else:
        return False



def main():
    number = int(input('number:'))
    if hws(number) ==True:
        print('这个函数是回文数！')
    else:
        print('这个函数不是回文数！')


if __name__ =='__main__':
    main()