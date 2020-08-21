"""
lesson1 : 写入二进制文件
描述：实现了复制图片文件的功能

Version : 0.1
Auther  : 郑超轩
"""
def main():
    file = None
    try:
         file = open('D:\图片\壁纸\动漫\c.png','rb')
         date = file.read()
         print(date)#打印大量二进制代码
         file2 = open("D:\Vistual studio editor\Code\python\day 11\动漫.jpg",'wb')
         file2.write(date)
    except FileNotFoundError:
        print('无法找到文件位置！')
    except IOError as E:
        print('无法写入文件！')
    finally:
        file.close()
        file2.close()
        print('程序结束！')
         

if __name__=="__main__":
    main()
