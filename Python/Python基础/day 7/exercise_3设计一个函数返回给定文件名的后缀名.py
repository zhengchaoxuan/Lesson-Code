"""
exercise3: 设计一个函数返回给定文件名的后缀名


Version : 0.1
Author  : 郑超轩
Date    : 2020/02/10
"""
"""
param:
    name : 文件名

return:
    name_back :后缀名(不带点)
"""

def return_hz(name):
    name_back = ''
    if name.find('.') != -1:
        name_position = name.find('.')+1
        for i in range(name_position,len(name)):
            name_back +=name[i]
    return name_back


def main():
    name = 'zhengchaoxuan.jpg'
    print(return_hz(name))

if __name__ == "__main__":
    main()


"""
参考答案：
param:
    filename: 文件名
    has_dot : 返回后面是否需要带点
return:
    name_dot: 文件后缀
def get_suffix(filename,has_dot=false):
    pos =filename.find('.')
    if 0 <pos<len(filename)-1:
        index = pos if has_dot else pos +1
        return filename[index:]
    else:
        return""
"""