"""
lesson1:用for循环实现1-100求和

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/20rr
"""
#range(101)可以产生一个0到100的整数序列。
#range(1, 100)可以产生一个1到99的整数序列。
#range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量
sum = 0;
for i in range(101):
    sum+=i;
print('sum= %d' % (sum))

"""
Verson : 0.2
功能：实现1-100的偶数相加
author : 郑超轩
Data   : 2020/01/20
"""
sum2 = 0
for i in range(2,101,2):
    sum2 += i
print('sum2= %d' % (sum2))

"""
lesson2:计算机出一个1~100之间的随机数，人输入自己猜的数字，计算机给出对应的提示信息，直到人猜出计算机出的数字

Verson : 0.1
Author : 郑超轩
Data   : 2020/01/20
"""

import random  #添加random
answer  = random.randint(1,100)
counter = 0
while True:
    counter +=1
    number=int(input('请输入一个数字 ： '))
    if number > answer:
        print('大了一点点！')
    elif number < answer:
        print('小了一点点！')
    else:
        print('恭喜你，答对了！')
        break
print('你在第 %d 次猜中了' % (counter))
if counter > 8:
    print('你的运气差了点！')
