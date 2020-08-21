# 该代码是python从入门到实践的练习源码
# date ：2020/07/20
# version : 0.1
# including : 
# 1.继承时用一个类的实例来当作属性
# 2.属性修改的三种方法（最方便的是直接修改）

# 9-1 餐馆
class Restaurant(object):
    # 餐馆属性：名字和类型
    def __init__(self,restaurant_name,restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
    
    #方法：描述餐馆
    def describe_restaurant(self):
        print(self.restaurant_name+"'s food is delicious!")
    
    #方法：描述是否营业
    def open_restaurant(self):
        print(self.restaurant_name+'is open!')

target_restaurant = Restaurant('KFC','Hamburger')

target_restaurant.describe_restaurant()
target_restaurant.open_restaurant()
print(target_restaurant.restaurant_name)
print(target_restaurant.restaurant_type)
print('\n')

# 9-4 就餐人数--在9-1中改良
class Restaurant1(object):
    # 餐馆属性：名字和类型
    def __init__(self,restaurant_name,restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.restaurant_number = 0
    
    #方法：描述餐馆
    def describe_restaurant(self):
        print(self.restaurant_name+"'s food is delicious!")
    
    #方法：描述是否营业
    def open_restaurant(self):
        print(self.restaurant_name+'is open!')
    
    # 方法：设置就餐人数
    def set_number_served(self,number):
        self.restaurant_number = number
    
    # 方法： 设置就餐人数增加
    def increment_number(self,number):
        if self.restaurant_number<100:
            self.restaurant_number+=number
        else:
            print('over the capacity of persons')
    
#9-6 冰淇淋小店
class IceCreamStand(Restaurant1):
    
    def __init__(self,restaurant_name,restaurant_type,flavors):
        super().__init__(restaurant_name,restaurant_type)
        self.flavors = flavors
    
    def show_icecream(self):
        print(self.restaurant_name+':')
        print(self.flavors)

my_icecream = IceCreamStand('zhengchaoxuan','IceCream',['a','b','c'])
my_icecream.show_icecream()

# 9-10 使用OrderedDict函数 --- 类，产生一个有序的空字典
from collections import OrderedDict
dictionary = OrderedDict()
dictionary ={
    'a':'A',
    'b':'B',
    'c':'C',
    'd':'D',
    'e':'E'
    }
for key,value in dictionary.items():
    print(key+' : '+value)

# 9-11 使用randint
from random import randint

#创建一个6面的色子
class Die(object):

    def __init__(self,sides=6):
        self.sides = sides
    
    #显示
    def show_die(self):
        print('色子的点数是: '+str(self.sides))

for i in range(10):
    x = Die(randint(1,6))
    x.show_die()






