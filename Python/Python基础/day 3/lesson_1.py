"""
lesson1:用户身份验证

Verson : 0.1
Author : 郑超轩
Data   : 2020/01/20
"""
username = input('请输入用户名 ：')
passord  = input('请输入密码 ：')
#如果用户名为admin,密码为：12345，则正确
if 'admin' ==username  and  '12345' ==passord:
    print('身份正确！')
else:
    print('身份错误！')  

print('\n\n\n')

"""
lesson2:分段求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Verson : 0.1
Author : 郑超轩
Data   : 2020/01/20
"""
#进行使用扁平结构而不是使用嵌套结构（可读性）
x = float(input('请输入x的值 ：'))
if x > 1:
    y = 3*x-5
    print('f(x)= %.2f' % (y))
elif x>=-1 and x<=1 :
    y = x+3
    print('f(x)= %.2f' % (y))
else:
    y = 5*x+3
    print('f(x)= %.2f' % (y))
    





