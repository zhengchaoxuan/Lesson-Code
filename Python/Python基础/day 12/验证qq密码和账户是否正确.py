"""
lesson 1: 验证输入用户名和QQ号是否有效并给出对应的提示信息
描述：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0

Author : 郑超轩
Date   : 2020.02.25
"""
#导入re模块
import re

def main():
    qq = input('请输入你的QQ账户:')
    passord = input('请输入你的QQ密码:')
    
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',passord)
    if not m1:
        print('密码错误！')
    
    m2 = re.match(r'^[1-9]\d{4,11}$',qq)
    if not m2:
        print('账户错误！')
    
    if m1 and m2:
        print("你输入的信息是有效的！")
if __name__ == "__main__":
    main()