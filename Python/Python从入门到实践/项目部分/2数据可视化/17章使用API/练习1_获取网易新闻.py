#获取网易新闻 https://api.apiopen.top/getWangYiNews
# date : 2020/08/11

import requests

url = 'https://api.apiopen.top/getWangYiNews'
r = requests.get(url)                   #获取URL信息
print('status code: ',r.status_code)    #核实是否调用成功，200
repo_dicts = r.json()       #生成字典，如何就可以当作字典处理
print(repo_dicts.keys())    #查看有哪些键 
print('reslut number: ',len(repo_dicts['result'])) #新闻个数

#输出新闻信息
news_dicts = repo_dicts['result']
for news in news_dicts:
    path_url = news['path']
    title = news['title']
    passtime = news['passtime']
    print('news title: ',title)
    print('news url: ',path_url)
    print('time: ',passtime)
    print('\n')


