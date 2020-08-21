"""
lesson1:继承问题
描述：
1）父类和派生类，super():super() 函数是用于调用父类(超类)的一个方法
2) 语法：super(type[, object-or-type])
3）# super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
4)Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
Version : 0.1
Author  : 郑超轩
Date    : 2020/02/14
"""
class Person(object):
    """父类"""

    def __init__(self,name,age):
        """初始化"""
        self._name = name
        self._age  = age
    
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
    @name.setter
    def name(self):
        self._name = name
        return self._name

    @name.setter
    def name(self):
        self._age = age
        return self._age
    
    def watch_tv(self):
        if self._age>=18:
            print("%s 正在看哥谭" % (self._name))
        else:
            print("%s 正在看喜羊羊" % (self._name))
    
class Student(Person):
    """派生类，增加，grade属性"""

    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self._gender = gender
    
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self):
        self._gender = gender
        return self._gender
    
    def study(self,course):
        print("%s 正在看 %s" % (self._name,course))
    

class Teacher(Person):
    """派生类，增加，title属性"""

    def __init__(self,name,age,title):
        #super(Teacher,self).__init__()  error
        #Person.__init__(self,name,age)  对
        super().__init__(name,age)
        self._title = title
    
    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self):
        self._title = title
        return self._title
    
    def study(self,course):
        print("%s 正在看 %s" % (self._name,course))    

#######################调用############################
"""    
def main():
    A = Student('郑超轩',38,'男')
    A.study('生活大爆炸')
    B = Teacher('雷军','48','男')
    B.study('小米')


if __name__ == "__main__":
    main()
"""

"""
lesson2 :多态
描述：
1）重写，抽象类（不可以创建对象的类，存在的目的就是让其他的类去继承它）
2）一般使用abc 类的ABCMeta元类和abstractmethod 
3)使用抽象氏，若实例需要添加别的属性，需要__init__，那么就需要使用到继承
Version : 0.1
Author  : 郑超轩
Date    : 2020/02/14
"""
from abc import ABCMeta,abstractmethod 
class Animal(object,metaclass=ABCMeta):
    """宠物"""

    def __init__(self,nickname):
        self._nickname  = nickname

    @abstractmethod
    def make_voice(self):
        """叫声"""
        pass

class Cat(Animal):

    def make_voice(self):
        print('%s :喵喵' % (self._nickname))

class Dog(Animal):
    def make_voice(self):
        print('%s :汪汪' % (self._nickname))
    


def main():
    cats = Cat('旺财')
    dogs = Dog('大黄')
    cats.make_voice()  #旺财：喵喵
    dogs.make_voice()  #大黄：汪汪

if __name__ =="__main__":
    main()



