"""
lesson2:访问可见性（公有和私有）  因为私有属性无法外部访问，所以一般不使用私有程序，一般用单下划线表示受保护的属性

Version : 0.1
Author  : 郑超轩
Date    : 2020/02/11
"""
# 一般不能在外部直接通过对象调用私有属性
# 但还是能通过内部方法调用对象的私有属性
class A(object):
    def __init__(self,foo):
        self.__foo = foo   # 一般不能在外部直接通过对象调用私有属性
    
    def __dar(self):   
        print(self.__foo)
        print('__dar')

def main():
    a1 = A('zheng')
    #a1.__dar()       #AttributeError: 'A' object has no attribute '__dar'--->私有格式
    #print(a1.__foo)  #AttributeError: 'A' object has no attribute '__foo'--->私有格式

    #但是python没有严格保证私有属性的私密性，可以使用更换名字的规定进行访问
    a1._A__dar()      # 但还是能通过内部方法调用对象的私有属性   #zheng  __dar
    print(a1._A__foo) #zheng
    


if __name__ =='__main__':
    main()
