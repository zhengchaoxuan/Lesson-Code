"""
lesson1 : socket套接字的客户端

Version : 0.1
Author  : 郑超轩
Date    : 2020/04/10
"""

from socket import socket

def main():
    #创建套接字
    client = socket()

    #进行连接服务器
    client.connect(('192.168.43.115',2000))

    #进行接收信息,每次最多为1024字节
    print(client.recv(1024).decode('utf-8'))

    #退出客户端
    client.close()




if __name__ == '__main__':
    main()