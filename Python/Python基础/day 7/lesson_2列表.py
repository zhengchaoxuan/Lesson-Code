"""
lesson1 : 列表的基本运算:结构化，非标量类型，使用[]

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/24
"""
list1 = [1,3,5,7,100]
print(list1) #[1,3,5,7,100]

#乘法表示列表的重复
list2 = ['hello'] * 3
print(list2)
list2[1] = 'w'
print(list2)   # hello,w,hello

#计算列表的长度(元素个数)
print(len(list1))

#下标（索引）运算
print(list1[0])   # 1
print(list1[4])   #100
print(list1[-1])  #100
print(list1[-3])  #5

#进行单个赋值
list1[1] = 100
print(list1) #1,100,5,7,100

#通过循环进行下标遍历列表元素
for index in  range(len(list1)):
    print(list1[index])

#通过for循环遍历列表元素
for elem in list1:
    print(elem)

#通过enumerate函数处理列表后进行遍历可以同时获得元素索引和值
for index,elem in enumerate(list1):
    print(index,elem)

print('\n\n\n')

"""
lesson2 :如何向列表中添加元素以及如何从列表中移除元素。

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/24
"""
list1 = [1,2,3,4,5]

#添加元素
list1.append(200)
print(list1) #[1,2,3,4,5,200]
list1.insert(1,100)
print(list1) #[1,100,2,3,4,5,200]

#合并两个列表
#list1.extend([1000,2000])
list1 += [1000,2000]
print(list1) #[1,100,2,3,4,5,200,1000,2000]

#先通过成员运算判断元素是否在列表中，如果在就删除
if 3 in list1:
    list1.remove(3)
print(list1) #1,100,2,4,5,200

#从指定的位置删除元素
list1.pop(0) #100,2,4,5,200

#清空列表元素
list1.clear()
print(list1) #[]

print('\n\n\n')

"""
lesson3 :切片操作

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/24
"""

fruits  = ['grape','apple','waxberry','strawberry']
fruits += ['pear']

#列表切片
fruits2 = fruits[2:4] #waxbery,strawberry,pear
print(fruits2)

#完整切片复制
fruits3 = fruits[:]
print(fruits3)

#反向切片，列表拷贝
fruits4 = fruits[-3:-1] #waxberry,strawberry
fruits5 = fruits[::-1]  #反过来

print('\n\n\n')

"""
lesson3 :排序操作

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/24
"""

list1 = ['grape','apple','waxberry','strawberry','pear']
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list2 = sorted(list1)
print(list2) #['apple', 'grape', 'pear', 'strawberry', 'waxberry']

#按开头字母从后面的到前面的
list3 = sorted(list1,reverse = True) #['waxberry', 'strawberry', 'pear', 'grape', 'apple']
print(list3)

#通过key 关键词指定字符串长度作为排序规则
list4 = sorted(list1,key = len)
print(list4)

"""
sort 与 sorted 区别：

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

"""
