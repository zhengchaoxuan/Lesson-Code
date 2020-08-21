'''实现randomwalk'''
import matplotlib.pyplot as plt
from random import randint

class randwalk(object):
    def __init__(self,walk_number=1000):
        self.walk_number = walk_number
        self.x_values = [0]
        self.y_values = [0]
    
    def randwalk_realize(self):
        while len(self.x_values)<self.walk_number:
            x_diction = [1,-1] #1代表x前进的方向，-1代表x后退的方向
            x_number = [0,1,2,3,4] #一步行走的步数
            y_diction = [1,-1]
            y_number = [0,1,2,3,4]

            x_step = x_diction[randint(0,1)]*x_number[randint(0,4)] #也可以使用chioce函数(需导入)
            y_step = y_diction[randint(0,1)]*y_number[randint(0,4)]
            x_position = self.x_values[-1]+x_step
            y_position = self.y_values[-1]+y_step
            self.x_values.append(x_position)
            self.y_values.append(y_position)


def main():
    while True:
        randwalks = randwalk(50000)
        randwalks.randwalk_realize()
        plt.figure(dpi= 128,figsize=(10,6))
        walk_numbers = list(range(randwalks.walk_number)) #用来进行颜色衍射
        plt.scatter(randwalks.x_values,randwalks.y_values,s=1,edgecolor='none',c = walk_numbers,cmap= plt.cm.Blues)

        #突出起点和终点
        plt.scatter(0,0,edgecolor= 'none',c = 'red',s =50)
        plt.scatter(randwalks.x_values[-1],randwalks.y_values[-1],c='red',edgecolor= 'none',s =50)

        #plt.title('随机漫步',fontsize = 16)
        plt.xlabel('number',fontsize = 8)
        plt.ylabel('square',fontsize = 8)


        #刻度设置
        plt.tick_params(axis='both',which ='major',labelsize = 10)

        #进行隐藏坐标轴
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        # 设置绘图窗口尺寸
        plt.show()

        #进行重置
        repeat = input('Make another walk?(y/n) ')
        if repeat == 'n':
            break

if __name__ == "__main__":
    main()



