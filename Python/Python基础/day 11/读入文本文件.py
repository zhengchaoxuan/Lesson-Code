"""
lesson1 : 读入文本文件

Version : 0.1
Author  : 郑超轩
Date    : 2020.02.22
"""
"""
def main():
    #读入文件，uft-8编码
    f = open("D:\Vistual studio editor\Code\python\day 11\案例.txt",'r',encoding="utf-8")
    print(f.read())
    f.close()
"""

"""
lesson1 : 读入文本文件--添加异常处理

Version : 0.2
Author  : 郑超轩
Date    : 2020.02.22
"""

from  time import sleep
def main():
    #方式1：读入文件，uft-8编码--finally释放资源
    """
    f=None
    try:
        f = open("D:\Vistual studio editor\Code\python\day 11\案例.txt",'r',encoding="utf-8")
        print(f.read())
    except FileNotFoundError:
        print('无法找到文件位置！')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('解码错误！')
    finally:
        if f:
            f.close()
    """

    #方式2--释放的方法不一样不要finally--with:关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
    """
    try:
        with open("D:\Vistual studio editor\Code\python\day 11\案例.txt",'r',encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print('无法找到文件位置！')
    except LookupError:
        print("指定的编码方式未知！")
    except UnicodeDecodeError:
        print('解码错误！')
    """

    #实现逐行输入
    #直接整个输入
    with open("D:\Vistual studio editor\Code\python\day 11\案例.txt",'r',encoding='utf-8') as f:
        print(f.read())
    #逐行输入
    with open("D:\Vistual studio editor\Code\python\day 11\案例.txt",'r',encoding='utf-8') as f:
        for line in f:
            print(line,end='')
            sleep(1)
    #逐行输入 ---readline
    with open("D:\Vistual studio editor\Code\python\day 11\案例.txt",'r',encoding='utf-8') as f:
        print(f.readline())

if __name__ =="__main__":
    main()