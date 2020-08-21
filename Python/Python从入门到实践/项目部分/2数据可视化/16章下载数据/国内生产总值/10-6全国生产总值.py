# 下载数据库进行包含全球大部分国家的国内2010年生产总值，绘制出图表
# author: 郑超轩
# date:2020/08/10
#步骤：导入数据-->进行国别码识别-->进行图形绘制
import json
from pygal_maps_world.i18n  import COUNTRIES
import pygal.maps.world
from  pygal.style import RotateStyle,LightColorizedStyle

#导入数据
def get_data(filename):
    productions = {} # 生产总值的字典
    try:
        with open(filename,'r') as f:
            productions = json.load(f)
    except FileNotFoundError:
        print('not find the filename')
    else:
        return productions

#进行国别码识别
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

def draw_figure(cc_productions):
    wm_style = RotateStyle('#3399AA',base_style= LightColorizedStyle)
    wm = pygal.maps.world.World(style = wm_style) #生成地图
    wm.title = 'GDP of all countries in 2010'
    wm.add('2010',cc_productions)
    wm.render_to_file('GDP of all countries in 2010.svg')

##生成新的字典过程，只保存code和value
def get_new_productions(productions,cc_productions):
    for production in productions:
        if production["Year"] == 2010:
            country_name = production["Country Name"]
            country_value = production["Value"]
            country_code = get_country_code(country_name)
            if country_code:
                cc_productions[country_code] = country_value

def main():
    filename = 'Python从入门到实践/项目部分/2数据可视化/国内生产总值/gdp_json.json'
    productions = get_data(filename)
    cc_productions = {} #生成新的字典，只保存code和value
    get_new_productions(productions,cc_productions)
    draw_figure(cc_productions)

if __name__ == "__main__":
    main()
            
            
