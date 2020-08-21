"""
exercise4:设计一个函数返回传入的列表中最大和第二大的元素的值

Version : 0.1
Author  : 郑超轩
Date    : 2020/02/11
"""
"""
param:
    list1: 输入函数的列表
return:
    max1 : 最大的元素的值
    max2 : 第二大元素的值
"""
def max_number(list1):
    max1,max2 = list1[0],list1[1] if list1[0]>list1[1] else (list1[1],list1[0])
    for index in range(2,len(list1)):
        if list1[index]>max1:
            max2 = max1
            max1 =list1[index]
        elif list1[index]>max2:
            max2=list1[index]
    return max1,max2

def main():
    list1 = [12,43,45,56,68,98,3,78,79,79]
    print(max_number(list1))

if __name__ =='__main__':
    main()