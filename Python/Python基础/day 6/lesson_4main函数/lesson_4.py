"""
lesson1:main函数的作用：调用模块时隐藏main函数里面的内容，除非直接使用含有main函数的Python文件

Version : 0.1
Author  : 郑超轩
Date   : 2020/01/22
"""

def foo():
    pass

def bar():
    pass

#__name__是Python中一个隐含的变量，它代表着模块的名字
#说明只要当Python解释器直接执行的模块名字才是_main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar() 