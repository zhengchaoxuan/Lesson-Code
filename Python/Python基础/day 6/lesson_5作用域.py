"""
lesson1 :函数的作用域问题：包含了全局作用域，局部作用域，嵌套作用域，内置作用域
内置作用域: input、 print、 int

Version : 0.1
Author  : 郑超轩
Date    : 2020/01/22
"""

def foo():
    b = 'hello'  #其对foo函数相当于内部作用域,对于bar函数相当于嵌套作用域
    #a=200       #内部作用域，其和全局作用域不通
    d= 30
    

    #函数内部再定义函数
    def  bar():
        c = True #bar函数的内部作用域
        nonlocal  d   #变量来自于嵌套作用域
        d = 10

        #print(a)
        print(b)
        print(c)

    bar() #调用bar函数
    print(d)

    global a
    a  = 200  # 使得全局变量 a = 200 

if  __name__ == '__main__':
    #a = 100  #if分支为全局变量
    
    foo()    #调用foo()函数 
    print(a)  #100