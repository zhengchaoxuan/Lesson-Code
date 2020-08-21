"""
lesson 1 : 从一段文字中提取出国内手机号码
描述：
1）使用findall直接返回返回字符串的列表
2）使用finditer返回迭代器--使用for循环
3) 使用search如果失败返回None --使用While

Author: 郑超轩
Date  : 2020.02.25
"""
import re

def main():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence ='''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    m1 = re.findall(pattern,sentence)
    print(m1)
    print("========================")

    m2 = re.finditer(pattern,sentence)

    for text in m2:
        print(text.group())
    print("========================")
    
    m3 = re.search(pattern,sentence)
    while m3:
        print(m3.group())
        m3 = pattern.search(sentence,m3.end())
        #print(re.search('重',sentence).end()) -->表示其索引值，返回匹配结束的下一个位置

if __name__ == "__main__":
    main()