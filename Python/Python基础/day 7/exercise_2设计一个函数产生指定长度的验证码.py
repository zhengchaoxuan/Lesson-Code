"""
exercise2:设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成（默认为4）

Version : 0.1
Author  : 郑超轩
Date    : 2020/02/10
"""

import random #引入随机函数库

def yzm(size=4):
    all_content = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all_size    = len(all_content)-1
    code  =''
    for i in range(4):
        code = code + all_content[random.randint(0,all_size)]
    return code

def main():
    print(yzm())   #默认设置长度为4

if __name__ == '__main__':
    main()

"""
参考答案：
import random ---直接用 random为[0,1)

作用：生成指定的验证码

param：
    code_len : 验证码长度(默认4个字符)

return:
    code : 验证码
def generate__code(code_len=4):
     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code
"""

