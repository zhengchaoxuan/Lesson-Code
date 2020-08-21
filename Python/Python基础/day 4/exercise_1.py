"""
exercise1:输入一个正整数判断是不是素数

Verson : 0.1
Author : 郑超轩
Date   : 2020/01/20
"""
number  = int(input('请输入一个正整数：'))
counter = 0
for i in range(2,number//2+2):
    if  (number%i == 0) and (number!=2):
        counter +=1
        break
if counter !=0 and number!=1:
    print('其不是素数！')
else:
    print("其是素数！")

#求素数循环结尾最好sqrt(number)+1
"""
Verson : 0.2
Author : 郑超轩
Date   : 2020/01/20
"""

from  math import sqrt
number  = int(input('请输入一个正整数：'))
counter = 0
end     = int(sqrt(number)) 
is_prime=True
for i in range(2,end+1):
    if  (number%i == 0) and (number!=2):
        is_prime=False
        break
if is_prime and number!=1:
    print('其是素数！')
else:
    print("其不是素数！")

print('\n\n\n')

"""
lesson_2:输入两个正整数，计算它们的最大公约数和最小公倍数

Verson : 0.1
Author : 郑超轩
DAte   : 2020/01/20
"""

x=int(input('x = '))
y=int(input('y = '))

if x>y:
    x,y = y,x

for factor in range(x,0,-1):
    if x%factor==0 and y%factor==0:
        print('公约数为%d' % (factor))
        print('公倍数为%d' % ((x*y)//factor))
        break

print('\n\n\n')
"""
lesson_3:打印三角形图形

Verson : 0.1
Author : 郑超轩
Date   : 2020/01/20
"""
x=int(input('请输入列数：'))
for a in range(1,x+1):
    for b in range(a):
        print('*',end='')
    print('\n')

for a in range(x):
    for b in range(x):
        if b < x-a-1:
            print(' ',end='')
        else:
            print('*',end='')
    print('\n')


for a in range(x):
    for b in range(x):
        if b<x-a-1:
            print(' ',end='')
    for i in range(a*2+1):
        print('*',end='')
    print('\n')
    



