"""
lesson1:可变容器模型，可存储任意类型对象（键和值通过冒号分开,并且匹配形成‘键值对’）

Version : 0.1
Author  : 郑超轩
Date    : 2020/02/05
"""

#创建字典的字面量语法
scores = {'郑超轩':99,'吴奇达':98}
print(scores)

#创建字典的构造器语法
items1 = dict(one = 1,two = 2,three = 3,four = 4)
print(items1)

#通过zip函数将两个序列压成字典
items2 = dict(zip(['a','b','c'],'123')) #{a:1,b:2,c:3}
print(items2)

#创建字典的推导式语法
items3 = {num : num**2 for num in range(1,10)}#{1:1,2:4,3:9.....,9:81}
print(items3)

#通过键获得字典中对应的值
print(scores['郑超轩']) #99
print(items1['one'])    #1

#对字典中所有键值进行遍历
for key in items3:
    print(f'{key}: {items3[key]}')  # 1:1  2:4  3:9  4:16

#更新字典的元素---直接添加和使用update添加多个
scores['郑超轩'] = 00
scores['诸葛亮'] =300
print(scores) #{'郑超轩': 0, '吴奇达': 98, '诸葛亮': 300}
scores.update(郑=10,吴=20)
print(scores) #{'郑超轩': 0, '吴奇达': 98, '诸葛亮': 300, '郑': 10, '吴': 20}

#判断语句
if '狄仁杰' in scores:
    print(scores['狄仁杰'])

#scores.get
print(scores.get('狄仁杰')) #none
print(scores.get('武则天',60))#60，不是添加到字典里面
print(scores) #{'郑超轩': 0, '吴奇达': 98, '诸葛亮': 300, '郑': 10, '吴': 20}


#删除字典中的元素
print(scores.popitem())#删除最后一个
print(scores)
print(scores.popitem())
print(scores)
print(scores.pop('郑超轩'))#删除特定的一个键
print(scores)
scores.clear()   #清空
print(scores)
