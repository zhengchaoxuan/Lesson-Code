"""
lesson 1: 替换字符串中的不良内容
描述：使用sub函数，返回字符串

Author : 郑超轩
Date   : 2020.02.25
"""
import re
def main():
    pattern = re.compile(r'[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',flags=re.IGNORECASE)
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    wm_sentence = re.sub(pattern,'*',sentence) #不可以在这里加入,flags=re.IGNORECASE -->ValueError: cannot process flags argument with a compiled pattern
    print(wm_sentence)

if __name__ == "__main__":
    main()