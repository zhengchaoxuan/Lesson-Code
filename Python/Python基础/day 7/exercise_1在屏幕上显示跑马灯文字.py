"""
exerciese1:在屏幕上显示跑马灯文字

Verison : 0.1
Author  : 郑超轩
Date    : 2020/02/10
"""

import os
import time

def main():
    content = "北京欢迎你的到来！！！"
    os.system('cls')  #清屏
    while True:
        print(content)
        time.sleep(0.2)  #休眠0.2s
        content  = content[1:] +content[0]

if __name__ =='__main__':
    main()