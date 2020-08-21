"""
lesson1 : Tread多线程处理
描述：https://www.php.cn/wenda/86278.html
1)join的问题（python多线程加了join函数为什么会变慢）：t.join()的意思是等待t这个线程执行结束后，在往下顺序执行语句。
如果不加的话，t还在执行中，然后就直接打印了print后面的内容，这个在你看来是运行结束了，但是其实t这个线程并没有结束。时间上是一样的。
Author  : 郑超轩
Date    : 2020.02.26
"""
from threading import Thread
from random  import randint
from time import time,sleep

def domnload(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    p1 = Thread(target =domnload,args = ('Python从入门到住院.pdf',))
    p1.start()
    p2 = Thread(target =domnload,args = ('Peking Hot.av',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))

    


if __name__ == "__main__":
    main()
