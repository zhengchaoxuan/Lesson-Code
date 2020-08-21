''' pygal置色子'''
# problem:
#1.件名不能命名成包的名字，python会调用这个自己编写的文件
# progress:
#1.进行简单的一个色子的编程绘制
#2.进行2个色子的编程设置

from random import randint
import pygal
class Die(object):
    def __init__(self,sizenumber=6):
        self.sizenumber = sizenumber
    
    def roll(self):
        return randint(1,self.sizenumber)

def main():
    die1 = Die()
    die2 = Die()
    results = []
    #进行100次循环
    for number in range(1000):
        number1 = die1.roll()
        number2 = die2.roll()
        number = number1+number2
        results.append(number)

    #获得1-6出现的次数
    frequents = []
    die_number = 2
    for value in range(1,die_number*die1.sizenumber+1):
        frequent = results.count(value) #统计字符串里某个字符出现的次数
        frequents.append(frequent)
    
    print(results)
    print(frequents)

    #进行直方图绘制
    hist = pygal.Bar()
    hist.title = 'Results Of Roll'
    hist.x_labels = map(str,range(1,die_number*die1.sizenumber+1))
    hist.x_title = 'Result'
    hist.y_title = 'Frequent'
    hist.add('D6',frequents)
    hist.render_to_file('Result.svg') 

if __name__ == "__main__":
    main()
        