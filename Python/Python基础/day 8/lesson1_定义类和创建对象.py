"""
lesson1:定义类class

Version : 0.1
Author  : 郑超轩
Date    : 2020/02/11
"""
class Student(object): #类名第一个一般规定大写
    
    #__init__是一个特殊方法用于创建对象时进行初始化操作
    #通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    
    def study(self,course_name):
        print('%s正在学习%s' % (self.name,course_name))
    
    def watch_movie(self):
        if self.age>=18:
            print('%s正在看哥谭'%(self.name))
        else:
            print('%s正在看喜羊羊'%(self.name))

def main():
    #创建学生对象
    #初始化学生对象名字和年纪
    stu1 = Student('郑超轩',20)
    #给对象发sudy消息
    stu1.study('Python')
    

    #给程序发watch_movie消息
    stu1.watch_movie()



if __name__  =="__main__":
    main()