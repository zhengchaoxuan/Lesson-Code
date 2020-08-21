"""
exercise1:华氏温度改为摄氏度

Version: 0.1
Author : 郑超轩
Data   : 2020/01/20
"""
temperature=float(input('请输入华氏温度：'))
temperature_s=(temperature-32)/1.8
print('%.1f 华氏温度变为摄氏温度为：%.1f' % (temperature,temperature_s))

"""
exercise2:输入圆的半径计算圆的周长和面积

Verson : 0.1
Author : 郑超轩
Data   : 2020/01/20
"""

r=float(input('请输入圆的半径：')) 
c=3.14*2*r #math.pi可以作为3.14，不过要添加import math
s=3.14*(r**2)

print('圆的周长为：%.2f' % (c))
print('圆的面积为：%.2f' % (s))

"""
exercise3:输入年份判断是不是闰年

Verson : 0.1
Author : 郑超轩
Data   : 2020/01/20
"""
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
year  = int(input('请输入年份：'))
judge = year % 4 # judge = ((year % 4)==0)得到judge=0/1
if 0 == judge:
    print('该年是闰年!')
else:
    print('该年不是闰年!')

