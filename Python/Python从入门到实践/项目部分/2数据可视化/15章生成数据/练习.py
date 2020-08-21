import matplotlib.pyplot as plt 

x_values =list(range(5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c = y_values,cmap= plt.cm.Blues,edgecolor= 'none',s=20)

plt.title('Squares Number',fontsize = 16)
plt.xlabel('number',fontsize = 8)
plt.ylabel('square',fontsize = 8)

#刻度设置
plt.tick_params(axis='both',which ='major',labelsize = 10)
plt.show()