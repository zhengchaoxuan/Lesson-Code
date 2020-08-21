"""
lesson1 : socket套接字的服务器

Version : 0.1
Author  : 郑超轩
Date    : 2020/04/10
"""

from datetime import datetime 
from socket import socket,SOCK_STREAM,AF_INET

def main():
    #创建socket对象(默认为ipv4和TCP套接字)
    # family=AF_INET 表示ipv4
    # family=AF_INET6 表示ipv6
    # type = SOCK_STREAM 表示TCP套接字
    # type = SOCK_DGRAM  表示UDR套接字
    # type = SOCK_RAW    表示原始套接字
    server = socket(family=AF_INET,type = SOCK_STREAM)

    #绑定IP地址和端口,同一时间只能绑定一个端口（区分服务）
    server.bind(('192.168.43.115',2000))

    #开启监听
    server.listen(512)
    print('服务器开始进行监听')

    while(True):
        #accept返回的第一个参数是客户端对象，第二个参数是客户端的地址（ip地址和端口）
        client,addr = server.accept()
        print(str(addr)+"连接到服务器")
        # 发送数据
        client.send(str(datetime.now()).encode("utf-8"))
        #结束发送
        client.close()


if __name__ == '__main__':
    main()