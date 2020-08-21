from threading import Thread
from  json import dumps #json.dumps()用于将dict类型的数据转成str
from socket import socket,SOCK_STREAM,AF_INET
from base64 import b64encode

def main():

    class add_server(Thread):
        def __init__(self,client,data):
            super().__init__()
            self.client = client
            self.data = data
        
        def run(self):
            #生成一个字典
            my_dict ={}
            my_dict['filename'] = 'texting.jpg'
            my_dict['filedata'] = self.data
            

            json_str = dumps(my_dict)

            self.client.send(json_str.encode('utf-8'))
            self.client.close()

    #创建socket对象
    server = socket(family=AF_INET,type = SOCK_STREAM)

    #设置ip地址和端口
    server.bind(('192.168.43.115',2000))

    #进行监听
    server.listen(512)
    print("进行服务器监听中..")
    #进行解码
    with open('d:/texting.jpg','rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    
    while True:
        client,addr = server.accept()
        add_server(client,data).start() #

        



if __name__ =="__main__":
    main()