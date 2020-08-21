import  pygal
from pygal.style import LightenStyle,LightColorizedStyle

chart_style = LightenStyle('#3399AA',base_style=LightColorizedStyle)
chart_config = pygal.Config()
chart_config.width = 500 #默认800
chart_config.x_label_rotation = 45 
chart_config.show_legend = False #隐藏图例

chart = pygal.Bar(chart_config,style = chart_style)
chart.title = 'Python Projects'
chart.x_labels = ['httpie','django','flask']

#2.2 添加自定义工具提示 ---- 字典：'value':数据进行绘制直线图，'label':描述数据的描述
plot_dicts = [{'value':10000,'label':'Description of httpie'},{'value':20000,'label':'Description of django'},{'value':30000,'label':'Description of flask'}]
chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')

