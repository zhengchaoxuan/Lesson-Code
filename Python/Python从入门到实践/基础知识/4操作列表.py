# 该代码是python从入门到实践的练习源码
# date ：2020/07/19
# version :0.1
# including:
# 1.直接使用列表进行循环（不需要索引）
# 2.使用for循环和range进行生成列表
# 3.列表切片和列表解析，列表复制和列表关联
# 4.一些简单的代码规范和不可修改的列表--元组

import time
#4-1 pizza
pizzas = ['a','b','c','d']
for pizza in pizzas:
    print('I like ' + pizza + ' pizza')
print('I really love pizza')

#4-2 animal
animals = ['dog','cat','mouse']
for animal in animals:
    print(f'A {animal} would make a great pet')
print('Any of these animals would make a great pet!')


#4-3
numbers = []
for number in range(1,21): #调整大小可以直接使用
    numbers.append(number)
print(numbers)

#4-4,5
numbers = []
for number in range(1,1000001): #调整大小可以直接使用
    numbers.append(number)
print(min(numbers))
print(max(numbers))
a = time.time()
sums = sum(numbers)
b = time.time()
print('耗时 '+str(b-a)+'s')
print("sums: "+str(sums))

#4-6 列表解析
numbers = [number for number in range(1,21) if number%2 !=0]
print(numbers)

#4-7 
numbers = [number**3 for number in range(1,11)]
print(numbers)

#4-10 切片
print('the first three items in the list are: '+ str(numbers[:3]))
print('Three items from the middle of the list are:'+str(numbers[4:7]))
print('the last three items in the list are: '+ str(numbers[-3:]))

#4-11 pizza续
friend_pizzas = pizzas[:] #进行复制，但是不产生关联
friend_pizzas.append('e') #朋友的pizza添加新的种类
print('my favorite pizzas are:')
for pizza in pizzas:
    print(pizza.title())

print("my friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())

#4-12 自助餐
print('\n')
buffets = ('a','b','c','d','e')
for food in buffets: #打印食物
    print(food) 
#buffets[0] = 'A'
buffets = ('A','B','c','d','e')
for food in buffets: #打印食物
    print(food)









