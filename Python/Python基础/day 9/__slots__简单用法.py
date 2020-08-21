"""
lesson2 : __slots__简单用法
描述：
1）如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量进行限定
2）__slots__的限定只对当前类的对象有效，对子类并不起任何作用

Version : 0.1
Author  : 郑超轩
Date    : 2020/02/12
"""
######################类的定义################
class Person(object):
    #限定Person对象只能绑定_name,_age,_gender属性
    __slots__ = ('_name','_age','_gender')

    def __init__(self,name,age):
        self._name = name
        self._age = age 
    
    @property
    def name(self):
        return self._name 
    
    @property
    def age(self):
        return self._age
    
    @name.setter
    def name(self,name):
        self._name = name
    
    @age.setter
    def age(self,age):
        self._age = age
    
################调用#############################
P = Person('郑',21)
P.name = '郑超轩'
print(P.name)

print(P.age)

P._gender = '男'
print(P._gender)
P._is_gay =True ## AttributeError: 'Person' object has no attribute '_is_gay'

