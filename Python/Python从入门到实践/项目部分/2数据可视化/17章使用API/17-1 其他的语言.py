# github生成其他语言的可视化 https://api.github.com/search/repositories?q=language:Java&sort=stars
# date : 2020/08/11

import requests
import pygal
from pygal.style  import LightColorizedStyle,LightenStyle

url = 'https://api.github.com/search/repositories?q=language:Java&sort=stars'
r = requests.get(url)                   #获取URL信息
print('status code: ',r.status_code)    #核实是否调用成功，200
repo_dicts = r.json()       #生成字典，如何就可以当作字典处理
print(repo_dicts.keys())    #查看有哪些键 
print('Total number: ',repo_dicts['total_count']) #总的项目数
print('Reslut number: ',len(repo_dicts['items'])) #探索的项目数

#进行输出项目的内容
items_dicts = repo_dicts['items']
names  = []
print('\nthe popular  Java repositories of Github:')
for items_dict in items_dicts:
    names.append(items_dict['name'])
    print("repository's name: ",items_dict['name'])
    print('owner name: ',items_dict['owner']['login'])
    print('html url: ',items_dict['html_url'])
    print('stars : ',items_dict['stargazers_count'])
    print('description: ',items_dict['description'])
    print('\n')

#进行pygal绘图
chart_style = LightenStyle('#3399AA',base_style= LightColorizedStyle)
chart_config = pygal.Config()
chart_config.title_font_size = 24
chart_config.x_label_rotation = 45
chart_config.major_label_font_size = 18
chart_config.label_font_size = 14
chart_config.truncate_legend = 15
chart_config.width = 800

chart = pygal.Bar(chart_config,style = chart_style)
chart.title = 'the popular  Java repositories of Github'
chart.x_labels = names

#生成列表
items_part_dicts = []
for items_dict in items_dicts:
    items_part_dict = {
        'value':items_dict['stargazers_count'],
        'label':items_dict['description'],
        'xlink':items_dict['html_url']
    }
    items_part_dicts.append(items_part_dict)

chart.add('Stars',items_part_dicts)
chart.render_to_file('17-1Java.svg')


