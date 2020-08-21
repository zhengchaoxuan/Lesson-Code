"""
lesson1 : 字符串

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/22
"""
#单个或多个字符用单引号或者双引号包围起来，就可以表示一个字符串
s1 = 'hello,world!'
s2 = "hello,world"

#以三个双引号或者单引号开头的字符串可以折行
s3 = """hello,
world! """

print(s1,s2,s3,end='')
"""
输出为：hello,world!hello,world!hello
world
"""
print('\n\n\n')

# Version : 0.2
# 使用 \ 进行转义
s4 = '\'hello,world!\'' #表示添加''号
s5 = '\n\\hello,world!\\\n'
print(s4,s5,end='')

print('\n\n\n')

# Version : 0.3
# \141和\x61都代表小写字母a，前者是八进制，后者是十六进制
# 在后面加上Unicode表示字符，例如 \u9a86\u660a代表的是中文“骆昊”
s6 = '\141\142\143\x61\x62\x63' #abcabc
s7 = '\u9a86\u660a'            
print(s6,s7)

print('\n\n\n')

# Version : 0.4
# 使用r加说明，表示 \ 不转义
s8 = r'\'hello,world!\''
s9 = r'\n\\hello, world!\\\n'
print(s8,s9,end='')

print('\n\n\n')

# Verson : 0.5
# 技巧：字符串使用 运算符

s10 = 'hello ' * 2        # hello hello
s11 = 'hello,' + 'world!' # hello,world!
print('he' in s1)         # True 判断一个字符串是否包含另外一个字符串（成员运算）
print('he' not in s1)     # False 

s12 = '123456789'

print(s12[0])             # 1
print(s12[2:5])           #345
print(s12[2:])            #3456789
print(s12[2::2])          #3579 ,间隔2
print(s12[::-1])          #987654321
print(s12[-3:-1])         #78

print('\n\n')

# Version : 0.6
# 技巧 ：使用字符串的函数 

str1 = "hello,world!"

#使用内置函数len计算字符串的长度
print(len(str1))         # 12 表示Python单纯是看多少个字符，其字符串不含换行符

# 拷贝字符串，首字母变成大写
print(str1.capitalize()) # Hello,world!

#拷贝字符串 ，每个单词首字母大写
print(str1.title())      # Hello,World!

#拷贝字符串，upper表示字符串变大写，lower表示字符串变小写
print(str1.upper()) #HELLO,WOELD!

#从字符串查找子串的位置，如果找不到输出-1
print(str1.find('or'))
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))

#查找字符串是否是以指定的字符串作为开头
print(str1.startswith('He')) #False
print(str1.startswith('he')) #True

#查找字符串是否是以指定的字符串作为结尾
print(str1.endswith('!'))     #True

#将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(15,'*'))    #先填充左边的

# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))

#检查字符串是否是数字构成
print(str1.isdigit())         #False

#检查字符串是否是字母构成
print(str1.isalpha())         #False 含有符号

# 检查字符串是否以数字和字母构成
print(str1.isalnum()) 

str2 = '  jackfrued@126.com '
print(str2)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str2.strip())

print("\n\n\n")

# Version : 0.7
# 技巧    : 格式化输出和字符串化输出

#格式化输出
a,b = 1,2
print('%d * %d = %d ' %(a,b,a*b))

#字符串输出
print('{0}*{1} = {2}'.format(a,b,a*b))
#简化
print(f'{a} * {b} = {a * b}')
