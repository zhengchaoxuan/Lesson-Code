"""
lesson1:生成斐波那契数列的前20个数特点是数列的前两个数都是1，
从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/21
"""
x_head = 1
x_back = 1
number = 0
while number < 10:
    print(x_head,x_back,sep=',',end=',')
    x_head = x_head + x_back
    x_back =x_back  + x_head
    number += 1

print('\n\n\n')
"""
lesson2:完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身.
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/21
"""
sum = 0 
for i in range(2,10001):
    for a in range(1,i):
        if i % a == 0:
            sum += a
    if sum == i :
        print(i,sep=',',end=',')
        sum = 0
    else:
        sum = 0


    

    