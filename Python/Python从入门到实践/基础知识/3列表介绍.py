# 该代码是python从入门到实践的练习源码
# date ：2020/07/18
# version :0.1
# including: 3-1,2,4,5,6,7,8
#3-1 打印名字
names = ['zheng','chao','xuan']
for i in range(len(names)):
    print(names[i])

#3-2 添加到问候语
names = ['zheng','chao','xuan']
for i in range(len(names)):
    print("欢迎"+names[i].title()+'到我校参观')

#3-4 嘉宾名单
guests = ['zhengchaoxuan','mery','wuqida']
for i  in range(len(guests)):
    print('I want you '+guests[i]+' to join my party')


#3-5修改嘉宾名单
print('\n')
no_guest = guests[2]
guests[2] = 'penyuyang'
print("we can't invite "+no_guest+' because he is not time')
for i  in range(len(guests)):
    print('I want you '+guests[i]+' to join my party')

#3-6添加嘉宾名单
print('\n')
guests.insert(0,'wmt')
guests.insert(int(len(guests)/2),'zcx')
guests.append('wz')
print('because I find a bigger table')
for i  in range(len(guests)):
    print('I want you '+guests[i]+' to join my party')

#3-7删减嘉宾名单
print('\n we can only invite 2 guests to join in my party')
for i in range(len(guests)-2):
    guests.pop()

for i in range(len(guests)):
    print('I want you '+guests[i]+' to join my party')

del guests[0]
del guests[0]
print(len(guests))

#3-8    
travel_place = ['shanghai','lasha','beijin','congqing','chengdu']
print(travel_place)
print(sorted(travel_place,reverse=True)) #按字母顺序输出（暂时）
print(travel_place)

travel_place.reverse()   #反转（永久）
print(travel_place)
travel_place.reverse()
print(travel_place)

travel_place.sort() #按字母顺序输出（永久）
print(travel_place)
travel_place.sort(reverse=True)
print(travel_place)

# index()方法在列表中查找值,如果该值存在于列表中，就返回它的下标。如果该值不在列表中，Python 就报ValueError。
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')


#引用的概念,copy的概念
from copy import copy,deepcopy
def a(a1):
    a1.append(6)

a1 = [1,2,3,4]
b1 = a1
b1.append(5)
print(a1) #1，2，3，4，5
a(a1)
print(a1) #1,2,3,4,5,6

c1 = copy(a1)
c1.append(7)
print(a1) #1,2,3,4,5,6


