"""
lesson1 : 使用列表生成器

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/26
"""
import sys
f = [x for x in range(1,10)]
print(f)

f = [x+y for x in 'ABCD' for y in '1234567']  #相当于嵌套循环
print(f) 

# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x**2 for x in range(1,3)]
print(f)
print(sys.getsizeof(f)) #44
f1 = [1,4]
print(sys.getsizeof(f1)) #36
print(sys.getsizeof(8)) #14
for val in f:
    print(val)  #1,4

"""
lesson2 : 使用yield关键字把一个普通函数改造成生成器函数

Verson : 0.1
Author : 郑超轩
Date   : 2020//26
"""
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b ,a+b
        yield a

def main():
    for val in fib(20):
        print(val)

if __name__ == '__main__':
    main()

