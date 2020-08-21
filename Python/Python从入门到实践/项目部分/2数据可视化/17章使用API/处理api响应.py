# 处理api响应
# date:2020/8/10

#唯一的一个非转基因的 Python HTTP 
#可能会因为网速等问题发生报错
import requests
import pygal
from pygal.style import LightColorizedStyle,RotateStyle,LightenStyle #进行颜色设置

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' 
r = requests.get(url) #获得响应对象
print('Status Code: ',r.status_code) #核实调用是否成功，200就是成功
response_dict = r.json()    #转换成字典格式
print(response_dict.keys()) #查看有哪些键

#可以按照字典来处理response_dict
repo_dicts = response_dict['items'] #获得items信息
print('repositories return: ',len(repo_dicts)) #探索有关仓库的信息

#显示第一个仓库的信息
repo_dict1 = repo_dicts[0]
print('key number:',len(repo_dict1)) 
for key in repo_dict1.keys(): 
    print(key)

#通过查看这些键，可以提取第一个项目的有效信息
print('\n Selcet information about first repository: ')
print('Name:',repo_dict1['name']) #项目名字
print('Login：',repo_dict1['owner']['login']) #所有者登录名字
print('Stars:  ',repo_dict1['stargazers_count']) #获得星数
print('Repository: ',repo_dict1["html_url"]) #github仓库的URL
print('Created ',repo_dict1["created_at"]) #创建时间
print('Updated ',repo_dict1["updated_at"]) #修改时间
print('description',repo_dict1['description']) #修改时间

#通过查看这些键，可以提取每个项目的有效信息
print('\n')
print('\nSelcet information about each repository: ')
for repo_dict in repo_dicts:
    print('Name:',repo_dict['name']) #项目名字
    print('Login：',repo_dict['owner']['login']) #所有者登录名字
    print('Stars:  ',repo_dict['stargazers_count']) #获得星数
    print('Repository: ',repo_dict["html_url"]) #github仓库的URL
    print('Created: ',repo_dict["created_at"]) #创建时间
    print('Updated:  ',repo_dict["updated_at"]) #修改时间
    print('Description: ',repo_dict['description']) #描述项目的信息
    print('\n')

#1.6. 使用pygal进行可视化设置 --字典：names,stars
names,stars = [],[] #进行bar的x,y设置
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

stars_chart_style = LightenStyle('#3399AA',base_style=LightColorizedStyle) #加亮
stars_chart = pygal.Bar(style = stars_chart_style,x_label_rotation=45)
stars_chart.title = 'popular python projects on github'
stars_chart.x_labels =names
stars_chart.add('stars',stars)
stars_chart.render_to_file('popular python projects on github plus.svg')

#2.1 改进pygal图表，增加了Config函数进行图表的配置
my_style = LightenStyle('#3399AA',base_style=LightColorizedStyle) #加亮
my_config = pygal.Config()              #配置实例
my_config.x_label_rotation = 45         #旋转45°
my_config.title_font_size = 24          #标题的大小
my_config.major_label_font_size = 18    #主标签大小
my_config.label_font_size = 14          #副标签大小
my_config.show_y_guides = False         #隐藏y辅助线
my_config.truncate_label = 15           #把较长的项目名缩短到15个值
my_config.width = 1000                  #图形宽度

plot_dicts = [] 
for repo_dict in repo_dicts:
    if  repo_dict['description']:
        plot_dict = {
            'value':repo_dict['stargazers_count'],
            'label':repo_dict['description'],
            'xlink':repo_dict["html_url"] #单击条形图可打开链接
        }
    else:
                plot_dict = {
            'value':repo_dict['stargazers_count'],
            'label':'None Description',
            'xlink':repo_dict["html_url"] #单击条形图可打开链接
        }
    plot_dicts.append(plot_dict)

chart = pygal.Bar(my_config,style = stars_chart_style)
chart.title = 'popular python projects on github'
chart.x_labels =names
chart.add('stars',plot_dicts)
chart.render_to_file('popular python projects on github plus config.svg')














