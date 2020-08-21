from matplotlib import pyplot as plt
from datetime import datetime
import csv

filename = 'Python从入门到实践/项目部分/2数据可视化/下载数据/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    row1 = next(reader)

    max_temperatures = []
    min_temperatures = []
    date = []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
            date.append(current_date)
        except ValueError:
            print(date,'miss dates')
        else:
            max_temperatures.append(high)
            min_temperatures.append(low)


fig = plt.figure(dpi = 128,figsize=(10,6))
plt.plot(date,max_temperatures,linewidth = 1,c='red')
plt.plot(date,min_temperatures,linewidth = 1,c='green')
plt.fill_between(date,max_temperatures,min_temperatures,facecolor = 'blue',alpha = 0.2)

plt.title('temperatures',fontsize = 24)
fig.autofmt_xdate() #x轴标签倾斜

plt.xlabel('',fontsize = 12)
plt.ylabel('max_temperature',fontsize = 12)
plt.tick_params(axis = 'both',labelsize = 12,which = 'major')
plt.show()
