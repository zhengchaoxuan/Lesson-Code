"""
lesson1:静态方法
描述：
1）该方法只适用于类，不适用于实例（因为对象还没创立），描述：@staticmethod
Version : 0.1
Author  : 郑超轩
Date    : 2020/02/13
"""
from math import sqrt

class Triangle(object):
    
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    
    @staticmethod
    def is_triangle(a,b,c):
        """判断是否是三角形"""
        return a+b>c and a+c>b and b+c>a 
    
    def perimeter(self):
        """周长"""
        perimeters = self.a +self.b +self.c
        return perimeters

    def area(self):
        """面积"""
        half_perimeter = (self.a +self.b +self.c)/2
        areas = sqrt(half_perimeter*(half_perimeter-self.a)*(half_perimeter-self.b)*(half_perimeter-self.c))
        return areas
    

def main():
    a,b,c = 3,4,5
    if Triangle.is_triangle(a,b,c):  #重点
        t = Triangle(a,b,c)
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t)
        print("其周长为 %02f" % (t.perimeter()))
        print("其面积为 %02f" % (t.area()))
    else:
        print('无法构成三角形！！！')

if __name__ == "__main__":
    main()

"""
Version 0.1: AttributeError: 'function' object has no attribute 'is_triangle'
"""

"""
lesson2 : 类方法
描述：
1）第一个参数是cls,它代表当前类相关的信息的对象--通过这次参数我们可以获得和类相关的信息并且创造出类的对象

Version : 0.1
Author  : 郑超轩
Date    : 2020/02/13
"""

from time import time ,localtime,sleep #time返回当前时间的时间戳（1970纪元后经过的浮点秒数）),localtime(格式化时间戳为本地的时间),sleep(休眠1s)

"""
描述一个时钟，开始值是现在的时间，只含hour,minute,second
1)__init__函数，一个确定现在的类方法，一个时间流程的实例方法，一个显示的实例方法
"""

class Clock(object):
    """时钟的类"""
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    @classmethod
    def now(cls):
        """现在"""
        times = localtime(time())
        return cls(times.tm_hour,times.tm_min,times.tm_sec)
    
    def clock_run(self):
        """时间流程"""
        self.second += 1
        if self.second>=60:
            self.minute += 1
            self.second = 0
            if slef.minute>=60:
                self.hour += 1
                self.minute=0
                if self.hour >=24:
                    self.hour =0
    
    def clock_show(self):
        """显示"""
        return "%02d : %02d : %02d " % (self.hour,self.minute,self.second)





def main():
    now_clock = Clock.now()
    while True:
        print(now_clock.clock_show())
        sleep(1)
        now_clock.clock_run()


if __name__ =="__main__":
    main()

