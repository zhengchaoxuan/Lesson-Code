import matplotlib.pyplot as plt

squares = [1,2,3,4,5]
number = [1,2,3,4,5]
plt.plot(number,squares,linewidth = 5) #plot函数：尝试根据数字绘制出有意义的图形
plt.title('Square Number',fontsize = 16) #标题，fontsize:字体大小
plt.tick_params(axis = 'both',labelsize = 10) #设置刻度标记大小

plt.xlabel('Value',fontsize = 10)
plt.ylabel('Number',fontsize = 10)

plt.show() # 打开 matplotlib查看器,并显示绘制的图像
