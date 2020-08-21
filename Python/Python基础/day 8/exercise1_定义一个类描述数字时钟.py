"""
exercise1:定义一个类描述数字时钟
描述：
1)from time import sleep
2)设置初始化时间
3）时钟的改变流程
4）时钟显示

Version : 1
Author  : 郑超轩
Date    : 2020/02/11
"""

from time import sleep

class time_clock(object):
    
    def __init__(self,hour=0,minute=0,second=0):
        self.hour   = hour
        self.minute = minute
        self.second = second
    
    def clock_run(self):
        """时间的流逝"""
        self.second+=1
        if self.second >= 60:
            self.minute += 1 
            self.second  = 0
            if self.minute >=60:
                self.hour += 1
                self.minute= 0
                if self.hour >= 24:
                    self.hour = 0

    def clock_show(self):
        """显示时间"""
        return "%02d :%02d :%02d " % (self.hour,self.minute,self.second)

def main():
    time1 = time_clock(12,23,35)
    while True:
        print(time1.clock_show())
        sleep(1)
        time1.clock_run()


if __name__ == '__main__':
    main()
"""
Version2 :添加了默认参数，把其他函数的参数除了self都删掉
Version3 :把其他函数中的hour添加self
Version4 : 使用return 作为 返回
"""

"""
参考答案：
from time import sleep


class Clock(object):
    数字时钟

    def __init__(self, hour=0, minute=0, second=0):
        初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        走字
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        显示时间
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
"""