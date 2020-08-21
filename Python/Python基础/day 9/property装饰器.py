"""
lesson1:property装饰器
描述：
1)什么是property特性：property装饰器用于将被装饰的方法伪装成一个数据属性，在使用时可以不用加括号而直接使用
注意:
    1. 定义时，在实例方法的基础上添加 @property 装饰器；并且仅有一个self参数
    2. 调用时，无需括号

2）可以进行当使用私有属性时，进行调用
Version : 0.1
Author  : 郑超轩
Date    : 2020/02/12
"""
"""简单的例子"""
class Goods(object):
    @property
    def size(self):
        return 199
#-----------------------
g = Goods()
print(g.size)

class Pager:
    def __init__(self,current_page):
        self.current_page = current_page 
        self.per_items    = 10

    @property
    def start(self):
        val = (self.current_page-1)*self.per_items
        return  val
    
    @property
    def end(self):
        val = (self.current_page)*self.per_items
        return val
#-----------------------------
p = Pager(10)
print(p.start)
print(p.end)

"""
property属性的俩种方式
1)装饰器:在方法上应用装饰器（推荐使用）
2）类属性: 即：在类中定义值为property对象的类属性（Python2历史遗留）

"""
"""1 装饰器"""
#经典类：只具有一种@property 装饰器 ---如上图

#新式类：具有三种@property装饰器 ------getter,setter,deleter

class Good(object):

    def __init__(self):
        #原价
        self.original_price = 100
        #折扣
        self.discount = 0.8
    
    @property
    def price(self):
        new_price = self.original_price*self.discount
        return new_price
    
    @price.setter
    def price(self,value):
        self.original_price = value
    
    @price.deleter
    def price(self):
        print('del')
        del self.original_price

orange = Good()
print(orange.price)  #获得商品价格

orange.price = 150
print(orange.price) #修改商品原价

del orange.price   #删除商品原价

#print(orange.price)  #获得商品价格 AttributeError: 'Good' object has no attribute 'original_price'


"""
类属性方式
property方法中有个四个参数
第一个参数是方法名，调用 对象.属性 时自动触发执行方法
第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
"""
#当使用类属性的方式创建property属性时，经典类和新式类无区别

#该例子和上面例子实现功能
class Go_od(object):
    def __init__(self):
        self.old_price = 200
        self.Discound  = 0.1
    
    def get_price(self):
        New_price = self.old_price*self.Discound
        return New_price
    
    def set_price(self,value):
        self.old_price = value
        return self.old_price
    
    def del_price(self):
        print('del')
        del self.old_price
    
    prices = property(get_price,set_price,del_price,"性价比高")


apple = Go_od()
 #使用get_price
print(apple.prices)

apple.prices=300
print(apple.prices)

#del apple.prices
a = Go_od.prices.__doc__
#a = apple.prices.__doc__错误 
print('%s'%(a))




    

