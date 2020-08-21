from socket import socket
from json import loads #二进制转化成字典格式
from base64 import b64decode

def main():
    #创建socket对象
    client = socket()

    #连接服务器
    client.connect(('192.168.43.115',2000))

    #接收原本的信息,每次最多1024个字节
    data = client.recv(1024)
    #创建二进制对象
    all_data = bytes()

    while(data):
        all_data +=data
        data = client.recv(1024)

    my_dicts = loads(all_data.decode('utf-8'))  #二进制转化字典

    filename = my_dicts['filename']
    filedata  = my_dicts['filedata'].encode('utf-8') #内容字典转化成二进制
    with open('e:/'+filename,'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
        print('图像已经保持')




if __name__ =="__main__":
    main()