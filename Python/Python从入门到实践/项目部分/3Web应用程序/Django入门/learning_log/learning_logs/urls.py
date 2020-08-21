'''定义learning_logs的URL模式'''
from django.urls import path,re_path
from . import views

app_name = 'learning_logs'

# 注意是列表要加逗号
urlpatterns = [
    #主页
    path('',views.index,name = 'index'),

    #显示所有的主题页面
    path('topics/',views.topics,name = 'topics'),
    #第三个实参将这个 URL 模式的名称指定为 topics ，让我们能够在代码的其他地方引用它。每当需要提供到这个主页的链接时，我们都将使用这个名称，而不编写 URL

    #特定主题页面
    re_path('topics/ (?P<topic_id>\d+)/$',views.topic,name = 'topic'), # ?P<topic_id> 将匹配的值存储到 topic_id 中；而表达式 \d+ 与包含在两个斜杆内的任何数字都匹配，不管这个数字为多少位

    #用来添加新主题的网页
    path('new_topic/',views.new_topic,name = 'new_topic'),

    #进行给主题添加新的条目
    re_path('new_entry/ (?P<topic_id>\d+)/$',views.new_entry,name = 'new_entry'),

    #编辑条目
    re_path('edit_entry/ (?P<entry_id>\d+)/$',views.edit_entry,name = 'edit_entry'),

    


]
