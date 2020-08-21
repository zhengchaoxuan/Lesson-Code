"""
使用变量保存数据并进行算术运算

Verson:1
Author:郑超轩
"""

a=321
b=123
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  #取整数部分
print(a%b)   #取余数
print(a**b)  #a的b次方

print('\n\n\n')

"""
使用type()检查数据类型

Verson:0.1
Author:郑超轩
Date:2020/01/20
"""

a=100
b=12.5
c=1+2j
d='hello'
e=True  #Bool类型第一位一定要大写

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print('\n\n\n')

"""
使用int()进行类型转换
使用input()进行输入
使用print()进行输出

Verson: 0.1
Author: 郑超轩
Data  : 2020/01/20
"""

a=int(input('a=')) #添加a=的目的是给予提示词
b=int(input('b='))

print('%d + %d = %d' % (a,b,a+b))  # %代表小数位占空符
print('%d / %d = %f' % (a, b, a / b))


print('\n\n\n')
"""
赋值运算符和复合赋值运算符的使用

Verson: 0.1
Author: 郑超轩
Data  : 2020/01/20
"""

a = 10
b = 5
a += b     #a=a+b
print(a)

a *= a+12  #a=a*(a+12)
print(a)


print('\n\n\n')
"""
比较，逻辑 运算符的使用

Verson: 0.1
Author: 郑超轩
Data  : 2020/01/20
"""
flag0 = 1==1 #逻辑
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag0 and flag2
flag4 = flag0 or  flag2
flag5=not (1 != 2)

print("flag0=",flag0)
print("flag1=",flag1)
print("flag2=",flag2)
print("flag3=",flag3)
print("flag4=",flag4)
print("flag5=",flag5)
print(flag1 is True)
print(flag2 is not False)