# 世界人口数据表
# author ： 郑超轩
# date: 2020/08/09
# 1.进行json文件的导入，并且知道Python不可以把包含小数点的字符串变成整数，需要字符串->浮点数->整数
# 2.获取两个字母的国别码（pygal的国别码）,并将没有国别码的国家直接使用国家名

#date;2020/08/10
# 3.绘制地图 -- 包括彩色区域，颜色标注，标签的地图
# 4.绘制地图 -- 显示国家人口数量
# 5.根据人口数量进行三种划分 --，1千万，10亿
# 6.进行颜色调整,让地图颜色更加统一--Rotatestyle - #wm_style是一个样式对象，第一个实参表示颜色，十六进制格式，分别表示红绿蓝的分量(RGB），第二个实参表示加亮颜色主题

from pygal_maps_world.i18n import COUNTRIES
import json
import pygal.maps.world #创建世界地图的库
from pygal.style import RotateStyle,LightColorizedStyle 

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code 
    return None

#导入json数据
filename = 'Python从入门到实践/项目部分/2数据可视化/制作世界人口数据/population_json.json'
with open(filename) as f:
    pop_numbers = json.load(f) #写入文件,保存原本的格式

#打印json文件
populations={} #进行保存国别码（国家名）和人口的字典
for pop_number in pop_numbers:
    if pop_number["Year"] == 2010:
        country_name = pop_number['Country Name']
        country_value= pop_number['Value']
        country_code = get_country_code(country_name)
        if country_code:
            populations[country_code] = country_value  
            print(str(country_code) +' : '+str(country_value))
        else:
            print(country_name+' : '+str(country_value))

populations1,populations2,populations3 = {},{},{}
for code,number in populations.items():
    if number<=10000000:
        populations1[code] = number
    elif number <=100000000:
        populations2[code] = number
    else:
        populations3[code] = number

wm_style = RotateStyle('#336699',base_style= LightColorizedStyle)
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'Population of World in 2010'
wm.add('number<=10m',populations1)
wm.add('10m<number<=1b',populations2)
wm.add('10b<=number',populations3)


wm.render_to_file('2010.svg')


