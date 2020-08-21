"""
exercise8 : 双色球选号
设计逻辑：
1)从1-33选6个不重复的数，再从1-16选一个数作为特码
2）一个函数进行操作流程，一个函数进行显示

Version : 0.1
Author  : 郑超轩
Date    : 2020/02/12
"""
from random import randint,sample #不重复 
def SSQ_run():
    all_number    =  [x for x in range(1,34)]
    select_number =  
    select_number =  sample(all_number,6)

    select_number.sort()
    select_number.append(randint(1,16))
    return select_number

def SSQ_show(select_number):
    for i in range(len(select_number)):
        if i !=len(select_number)-1:
            print("%02d " % (select_number[i]),end='')
        else:
            print(" | %02d " % (select_number[i]),end='')
    print()

def main():
    n = int(input('请输入几注:'))
    for i in range(n):
        SSQ_show(SSQ_run())


if __name__ =="__main__":
    main()
