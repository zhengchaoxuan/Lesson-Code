''' 散点图'''
# date : 2020/07/26
# 1.设置颜色 -- color
# 2.进行颜色的衍射 cmap 参数 -- c = y_values , cmap  = plt.cm.Blues cmap里面有很多的颜色参数
# 3.进行图形保存，savefig函数
import matplotlib.pyplot as plt

#x_value = [1,2,3,4,5]
#y_value = [1,2,3,4,5]
x_values = list(range(100))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s = 20,c = y_values,cmap = plt.cm.Blues ,edgecolor = 'none') #删除数据点的轮廓 color = （0，0，0.8）
plt.title('Squares Number',fontsize = 16)
plt.xlabel('number',fontsize = 8)
plt.ylabel('square',fontsize = 8)

#刻度设置
plt.tick_params(axis='both',which ='major',labelsize = 10)
plt.show()
plt.savefig('散点图.png',bboxs_inches = 'tight')
