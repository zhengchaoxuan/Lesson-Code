# 该代码是python从入门到实践的练习源码
# date ：2020/07/21
# version : 0.1

class Employee(object):
    """添加属性"""
    def __init__(self,supname,name,salary):
        self.supname = supname
        self.name = name
        self.salary = salary
    
    """年薪增加"""
    def give_raise(self,raise_money=1000):
        self.salary +=raise_money
    
    



