"""
lesson1:元组的基本操作(),区别：元组的元素不能修改,如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组

Version : 0.1
Author  : 郑超轩
Date    : 2020/01/26
"""

#定义元组
t = ('郑超轩','湖南永州',20,True)
print(t)

#获得元组的元素
print(t[0])
print(t[3])

#遍历元组的值
for mumber in t:
    print(mumber)

# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
print(t)

#将元组转换成列表
person = list(t)
print(person)

#列表是可以修改它的元素
person[0] = '李小龙'
person[1] = 25
print(person)

#将列表转换成元组
fruits_list  = ['apple','banana','orange']
fruits_tuple =tuple(fruits_list)
print(fruits_tuple)


"""

 元组的优点：
 1.元组的元素是无法修改的，便于系统安全
 2.元组在创建时间和所需的空间都优于列表
"""