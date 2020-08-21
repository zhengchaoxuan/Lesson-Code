# 该代码是python从入门到实践的练习源码
# date ：2020/07/18
# version :0.1
# include: 2-3,4,5,6,7,9

#2-3
name = 'zhengchaoxuan'
message = f"hello {name} ,world you like to learn some python today" # f格式化
print(message)

#2-4
print(name.capitalize()) #首字母大写
print(name.title())      #单词第一个大写
print(name.lower())      # 全部小写
print(name.upper())      # 全部大写

#2-5 
print('Albert Einstein once said,"A person who never made a mistake never tried anything new"')

#2-6
famous_person =   'Albert Einstein once said'
message = famous_person + ',"A person who never made a mistake never tried anything new"' # 拼接
print(message)

#2-7
name_ = "\tzhengchaoxuan\t"
print(name_.rstrip())  #去除后面的空白
print(name_.lstrip())  #去除前面的空白
print(name_.strip())   #去除两边的空白

#练习
name1 = 12
name = str(name1)
print(name[0])

#2-9
number = 4
message = 'my like number is' + str(number)
print(message)

# isX 字符串方法
a = 'Hello123'
print(a.isupper())
print(a.isalnum())

# 字符串方法 startswith()和 endswith()startswith()和 endswith()方法返回 True，
# 如果它们所调用的字符串以该方法传入的字符串开始或结束。否则，方法返回 False。
print('Hello world!'.startswith('Hello'))




