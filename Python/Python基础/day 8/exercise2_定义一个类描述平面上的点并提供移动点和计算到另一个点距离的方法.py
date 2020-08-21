"""
exercise2:定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
描述：
1)一个初始化  __init__
3)一个改变移动点位置    move_by
4）一个到另外一个点的距离 distance

Version : 1
Author  : 郑超轩
Date    : 2020/02/11
"""
from math import sqrt
class  Point(object):
    """初始化"""
    def __init__(self,x=0,y=0):
        self.x =x
        self.y =y

    def move_by(self,dx,dy):
        """移动"""
        self.x +=dx
        self.y +=dy

    def distance(self,other):
        """计算距离"""
        distance_x   = self.x - other.x 
        distance_y   = self.y - other.y
        distance_all = sqrt(distance_x**2+distance_y**2)
        return distance_all

    def __str__(self):
        """描述对象,字符"""
        return "%s ,%s" % (str(self.x),str(self.y))

def main():
    p1 =Point(3,8)
    p2 =Point()
    p1.move_by(-1,2)
    #1. print(p1)  直接使用会出现错误，<__main__.Point object at 0x03759160>  -->改变方法：加入__str__函数，返回一个字符串，当做这个对象的描写
    print(p1)
    print(p1.distance(p2))

if  __name__ == "__main__":
    main()