"""
lesson1:Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算

Version : 0.1
Author  : 郑超轩
Date    : 2020/01/30
"""
 # 创建集合的字面量语法
set1 = {1,2,3,3,3,2}
print(set1) #{1,2,3}
print('lenth = ',len(set1)) # 3
 
 # 创建集合的构造体语法
set2 = set(range(1,10))  #{1,2,3,4,5,6,7,8,9}
set3 = set((1,2,3,3,2,1))#{1,2,3}
print(set2,set3)

 # 创建集合的推导式
set4 = {num for num in range(1,100) if num % 3 ==0 and num % 5 ==0}
print(set4)

 # 添加元素和删除元素
set5 = {1,2,3}
set5.add(4)
set5.add(5)
print(set5)  #{1，2，3，4，5}
set5.update([12,13])
print(set5)  #{1，2，3，4，5，12，13}

 # 区别就是remove的元素在set当中没有的话会报错，而discard不会
set5.discard(3)
print(set5)  #{1，2，4，5，12，13}
set5.remove(4)
print(set5)

print(set5.pop()) # 1
print(set5)       # 2,4,12,13

 # 集合的交，并集，差集等运算
print(set1 & set2)
#print(set1.intersection(set2))

print(set1 | set2)
#print(set1.union(set2))

print(set1-set2)
#print(set1.difference(set2))

print(set1 ^ set2)
#print(set1.symmetric_difference(set2))

#判断子集和超集
print(set2 <= set1)  #set1是不是set2的子集
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))

 