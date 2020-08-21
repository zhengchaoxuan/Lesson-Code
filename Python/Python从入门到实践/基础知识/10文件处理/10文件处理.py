# 该代码是python从入门到实践的练习源码
# date ：2020/07/20
# version : 0.1

#练习1 --with关键字---在不需要访问文件后将其关闭
with open('D:/Vistual studio editor/Code/Python/Python从入门到实践/基础知识/10文件处理/pi_digits.txt','r') as file_name:
    content = file_name.read() #read()函数到文件末尾会加一个空字符串
    print(content.rstrip())

#练习2 -- 在每行的后面有一个换行符，所以在使用Print会出现/n/n的现象，可以使用rstrip函数
file_name = 'D:/Vistual studio editor/Code/Python/Python从入门到实践/基础知识/10文件处理/pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

#练习3 -- readlines()函数 从文件读取每一行，并将其存储在一个列表
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in  lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
print('\n')

#10-1 Python 学习笔记
file_name = 'D:/Vistual studio editor/Code/Python/Python从入门到实践/基础知识/10文件处理/Python.txt'
with open(file_name) as file_object: #只打印一个，使用要分别进行with
    #直接打印
    print(file_object.read())
    #遍历打印
with open(file_name) as file_object: #只打印一个，使用要分别进行with
    for line in file_object:
        print(line.rstrip())

    #存储在列表打印
with open(file_name) as file_object: #只打印一个，使用要分别进行with
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
print("\n")
# 10-2 使用replace函数进行替换
file_name = 'D:/Vistual studio editor/Code/Python/Python从入门到实践/基础知识/10文件处理/Python.txt'
with open(file_name) as file_object:
    content = file_object.read()

content = content.replace('Python','C')
print(content)

# 10-3 访客
user_name = input('enter your name: ')
file_name = 'D:/Vistual studio editor/Code/Python/Python从入门到实践/基础知识/10文件处理/name.txt'
with open(file_name,'w') as file_object:
    file_object.write(user_name)
    print('welcome to report your name!')

