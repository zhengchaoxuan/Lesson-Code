"""
lesson 1 : 实现Tread函数的继承--使用新的类进行继承Thread类

Author : 郑超轩
Date   : 2020.02.26
"""
from random import randint
from threading import Thread
from time import time, sleep

class Domnload_tasking(Thread):
    """继承Tread线程"""
    def __init__(self,filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s..' % (self._filename))
        time_to_domnload = randint(2,5)
        sleep(time_to_domnload)
        print('下载完成%s，用时%d秒' % (self._filename,time_to_domnload))

def main():
    start = time()
    t1 = Domnload_tasking('Python从入门到住院.pdf')  
    t1.start()
    t2 = Domnload_tasking('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("下载完成!一共用时%.1f"%(end-start))
    

if __name__ == '__main__':
    main()