# 世界人口数据图，覆盖全部国家，包括无法显示国别码的10多个国家
# author ： 郑超轩
# date: 2020/08/09


from pygal_maps_world.i18n import COUNTRIES
import json
import pygal.maps.world #创建世界地图的库
from pygal.style import RotateStyle,LightColorizedStyle 

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code 
        elif name == 'Yemen, Rep':
            return 'ye'
        elif name =='Vietnam':
            return 'vn'
        elif name =='Venezuela, RB ':
            return 've'
        elif name =='Tanzania':
            return 'tz'
        elif name =='South Sudan':
            return 'sd'
        elif name =='North Macedonia':
            return 'mk'
    return None

#导入json数据
filename = 'Python从入门到实践/项目部分/2数据可视化/制作世界人口数据/population_json.json'
with open(filename) as f:
    pop_numbers = json.load(f) #写入文件,保存原本的格式

#打印json文件
populations={} #进行保存国别码（国家名）和人口的字典
n=0
for pop_number in pop_numbers:
    if pop_number["Year"] == 2010:
        country_name = pop_number['Country Name']
        country_value= pop_number['Value']
        country_code = get_country_code(country_name)
        if country_code:
            populations[country_code] = country_value  
            print(str(country_code) +' : '+str(country_value))
        else:
            n+=1
            print(country_name+' : '+str(country_value))

print('n='+str(n))
populations1,populations2,populations3 = {},{},{}
for code,number in populations.items():
    if number<=10000000:
        populations1[code] = number
    elif number <=100000000:
        populations2[code] = number
    else:
        populations3[code] = number

wm_style = RotateStyle('#3399AA',base_style= LightColorizedStyle)
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'Population of World in 2010'
wm.add('number<=10m',populations1)
wm.add('10m<number<=1b',populations2)
wm.add('10b<=number',populations3)


wm.render_to_file('2010 Plus.svg')