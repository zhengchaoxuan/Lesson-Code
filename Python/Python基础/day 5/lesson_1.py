#构造程序逻辑：这个单元主要是进行把实际问题转变成Python逻辑
#经典例子
"""
lesson1:寻找全部水仙花数（水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。）

Version : 0.1
Author  : 郑超轩
Date    : 2020/01/21
"""

for i in range(100,1000):
    x_100 = i // 100
    x_10  = (i-x_100*100) // 10
    x_1   = i - x_100*100 - x_10*10
    if (x_100**3 + x_10**3 + x_1**3) == i:
        print('这是一个水仙花数： %d ' % (i))

#实现整数反转：将12345变成54321
#Verson : 0.1
x  = int(input('请输入一个正整数：'))
x1 = x
x2 = 0
while x1 > 0:
    x3 = x1 %10
    x1 = x1 //10
    x2 = (x2+x3)*10
print("反转为 %d" % (x2//10))

#Verson : 0.2
number = int(input('number = '))
change_number = 0
while number > 0:
    change_number = number%10+change_number*10
    number //=10
print("反转为 %d" % (change_number))

print('\n\n\n')
"""
lesson2:公鸡5元一只，母鸡3元一只，小鸡1元三只，
用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

Version : 0.1
Author  : 郑超轩
Date    : 2020/01/21
"""
#暴力搜索法（穷举法）
for z in range(300):
    if z % 3 == 0:
        for  y in range(100):
            for x in range(100):
                if 5*x + 3*y +z/3 == 100 and x+y+z == 100:
                    print('公鸡:%d 只，母鸡：%d 只 ，小鸡 %d 只' % (x,y,z))



"""
lesson3:CRAPS赌博游戏规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。

Version : 0.1
Author  : 郑超轩
Date    : 2020/01/21
"""

#first,second代表2个骰子
from random import randint

cost     = int(input('请输入你的全部筹码(必须为正整数)：'))
one_cost = int(input('请输入你的参与这次游戏的筹码(必须为正整数)：'))
remain   = cost - one_cost
first    = randint(1,6)
second   = randint(1,6)
one_1    = 0  
one_all  = 0  #表示第几轮
while  remain >= 0:
    all     =  first + second
    one_1   += 1
    one_all += 1
    if one_1 == 1:
        if first+second ==7 or first+second ==11:
            remain = remain + 2*one_cost
            print('you win in %d!' % (one_1))
            print('you have money:%d ' % (remain) )
        elif first+second ==2 or first+second ==3 or first+second==12:
            print('you lost in %d!' % (one_1))
            print('you have money:%d ' % (remain) )
        else:
            while True:
                one_1   += 1
                first    = randint(1,6)
                second   = randint(1,6)
                if first+second ==7:
                    print('you lost in %d!' % (one_1))
                    print('you have money:%d ' % (remain) )
                    break
                elif all == first + second:
                    remain = remain + 2*one_cost
                    print('you win in %d!' % (one_1))
                    print('you have money:%d ' % (remain) )
                    break
                else:
                    continue
    one_1=0
    one_cost = int(input('请输入你的参与这次游戏的筹码(必须为正整数)：'))
    remain   = remain - one_cost
    first    = randint(1,6)
    second   = randint(1,6)
print('you have no money!!!')
print('you in %d lost all money' % (one_all))



                






            
    
    

