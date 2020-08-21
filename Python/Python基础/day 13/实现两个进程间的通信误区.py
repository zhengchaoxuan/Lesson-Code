"""
lesson 1 : 实现两个进程间的通信误区
注意：
输出：ping和gong各10个，当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，
    每个子进程有自己独立的内存空间，这也就意味着两个子进程中各有一个counter变量，所以结果也就可想而知了
解决方法：比较简单的办法是使用multiprocessing模块中的Queue类
Author : 郑超轩
Date   : 2020.02.26
"""
from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)

        
def main():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()


if __name__ == '__main__':
    main()