"""
exercise1:英寸和厘米的换算

Verson : 0.1
Author : 郑超轩
Data   : 2020/01/20
"""
value = float(input("请输入长度: "))
unit  = input('请输入单位：')
if unit !='英寸' and unit !='厘米':
    print('输入单位错误！')
else:
    if unit == '英寸':
        value_change = value*2.54
        print('%f 英寸换算厘米为：%f ' % (value,value_change))
    else:
        value_change = value/2.54
        print('%f 厘米换算英寸为：%f ' % (value,value_change))


"""
exercise2:百分制成绩转换为等级制成绩

Verson : 0.1
Author : 郑超轩
Data   : 2020/01/20
"""
score = float(input('请输入你的成绩：'))
if score>=90:
    print('A')
elif score>=80 and score<90:
    print('B')
elif score>=70 and score<80:
    print('C')
elif score>=60 and score<70:
    print('D')
else:
    print('E')

"""
exercise3:判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/20
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a+b>c and a+c>b and b+c>a:
    perimeter = a + b + c

    #根据海伦公式 p = (a+b+c)/2 ,area=(p*(p-a)*(p-b)*(p-c))^1/2
    p    =perimeter/2 
    area =((p*(p-a)*(p-b)*(p-c)))**(1/2) 

    print('三角形周长为：%.2f' % (perimeter))
    print('三角形面积为：%.2f' % (area))
else:
    print('无法构成三角形！')