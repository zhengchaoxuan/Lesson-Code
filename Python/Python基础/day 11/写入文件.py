"""
lesson1 : 写入文件
描述：
如何将1-9999之间的素数分别写入三个文件中
（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）

Version : 0.1
Author  : 郑超轩
Date    : 2020.02.22
"""
from math import sqrt

def is_prime(number):
    assert number>0
    for x in range(2,int(sqrt(number))+1):
        if number % x == 0 and number !=2:
            return  False
    return True if number !=1 else False 

def main():
    filenames = ['D:\Vistual studio editor\Code\python\day 11\c.txt','D:\Vistual studio editor\Code\python\day 11\d.txt','D:\Vistual studio editor\Code\python\day 11\e.txt']
    file_list = []
    try:
        for filename in filenames:  
            file_list.append(open(filename,'w',encoding = 'utf-8'))
        for i in range(1,10000):
            if i<100 and is_prime(i):
                file_list[0].write(str(i)+'\n')
            elif i<1000 and is_prime(i):
                file_list[1].write(str(i)+'\n')
            elif i<10000 and is_prime(i):
                file_list[2].write(str(i)+'\n')
    except IOError as ex:
        print(ex)
        print('写入文件错误')
    finally:
        for file in file_list:
            file.close()
    

                


                
if __name__=="__main__":
    main()