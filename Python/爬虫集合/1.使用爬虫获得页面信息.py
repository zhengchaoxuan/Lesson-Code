# 1、为什么要设置headers?在请求网页爬取的时候，输出的text信息中会出现抱歉，
#无法访问等字眼，这就是禁止爬取，需要通过反爬机制去解决这个问题。headers是解决requests请求反爬的方法之一，相当于我们进去这个网页的服务器本身，假装自己本身在爬取数据

#3、headers中有很多内容，主要常用的就是user-agent 和 host，他们是以键对的形式展现出来，
#如果user-agent 以字典键对形式作为headers的内容，就可以反爬成功，就不需要其他键对；否则，需要加入headers下的更多键对形式。
import requests
from bs4 import BeautifulSoup

def get_url(url):
    #使用反爬机制，模拟使用页面
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    r = requests.get(url,headers = headers)
    return r.text

def get_content(html,page):
    output = """第{}页 作者：{} 性别：{} 年龄：{} 点赞：{} 评论：{}\n{}\n------------\n""" # 最终输出格式
    Soup = BeautifulSoup(html,'html.parser') #进行语法剖析
    Con = Soup.find(class_='content-block clearfix')  # 如图一红色方框
    Content_list = Con.find_all('div',class_ = 'article')
    for i in Content_list:
        name = i.find('h2').string
        author_info = i.find('div',class_ = 'articleGender')
        Smiles = i.find('div',class_ = 'stats').find(class_='stats-vote').find('i',class_='number').string
        Comment = i.find('div',class_ = 'stats').find(class_='stats-comments').find('i',class_='number').string
        Content =i.find('div',class_ = 'content').find('span').get_text()
        
        if author_info is not None:
            if  'womenIco' == author_info['class']:
                sex = '女'
                
            elif 'menIco' == author_info['class']:
                sex = '男'
            else:
                sex = ' '
            age = author_info.string
        else:
            sex = ' '
            age = ' '

        write_txt(output.format(page,name,sex,age,Smiles,Comment,Content))

#其为元组的格式
def write_txt(*args):
    for i in args:
        with open('output.txt','a',encoding='utf-8') as f:
             f.write(i)        

def main():
    for i in range(1,11):
        #获得1-10页的URL
        url = "https://www.qiushibaike.com/text/page/{}".format(i)
        Html = get_url(url)
        #解析页面
        get_content(Html,i)

if __name__ == "__main__":
    main()
