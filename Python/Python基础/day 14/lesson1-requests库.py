"""
lesson1 : 学习requests库的基础应用

Version : 0.1
Author  : 郑超轩
Date    : 2020/04/10
"""

from threading import Thread
import requests


def main():
    #天行数据，10代表个数
    repo = requests.get("http://api.tianapi.com/huanbao/index?key=6e3eb02b4a6753c315b6f9ab809d6cdd&num=10")
    date_repo = repo.json()

    for camera_date in date_repo["newslist"]:
        url = camera_date['picUrl']
        get_cameradate(url).start()



class get_cameradate(Thread):
    
    #参数信息
    def __init__(self,url):
        super().__init__()
        self.url = url
    
    #线程
    def run(self):
        filename = self.url[self.url.rfind('/')+1:]

        if(self.url.find("http")!=-1):
            repo = requests.get(self.url)
            with open("d:/"+filename,'wb') as f:
                f.write(repo.content)


    



if __name__ == "__main__":
    main()