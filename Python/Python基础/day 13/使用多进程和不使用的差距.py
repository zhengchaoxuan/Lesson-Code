"""
lesson 1 : 使用多进程和不使用多进程到底有什么差别
注意：
1）使用getpid获得子进程的ID
2）使用Process要注意，target是函数名字，args是参数要加括号且加逗号，表示多个参数
3）start方法用来启动进程，而join()方法表示等待子进程结束以后再继续往下运行，通常用于进程间的同步,有阻塞作用

Author : 郑超轩
Date   : 2020.02.26
"""
from multiprocessing import Process
from os import getpid #进程ID
from random import randint
from time import time,sleep

def NP_download_task(filename):
    print("开始下载%s" % (filename))
    time_to_domnload = randint(2,5)
    sleep(time_to_domnload)
    print('下载完成！耗费%d秒' % (time_to_domnload))

def P_domnload_task(filename):
    print('启动下载进程，进程号[%d]' % (getpid()))
    time_to_domnload = randint(2,5)
    sleep(time_to_domnload)
    print('下载完成！耗费%d秒' % (time_to_domnload))


def main():
    """不使用进程"""
    start = time()
    NP_download_task("Python从入门到住院pdf")
    NP_download_task("钢铁侠.mp4")
    end   = time()
    print('不使用多进程一共耗时%.1f' % (end-start))

    """使用进程"""
    p_start = time()
    p1 = Process(target = P_domnload_task,args =("Python从入门到住院pdf",))
    p1.start()
    p2 = Process(target = P_domnload_task,args =("钢铁侠.mp4",))
    p2.start()
    p1.join()
    p2.join()
    p_end   = time()
    print('使用多进程一共耗时%.1f' % (p_end-p_start))
    
if __name__ == '__main__':
    main()

