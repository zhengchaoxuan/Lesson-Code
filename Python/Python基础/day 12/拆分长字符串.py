"""
lesson 1 : 拆分长字符串

Author: 郑超轩
Date  : 2020.02.25
"""
import re

def main():
    pattern = re.compile(r'[，。,.]')
    sentence='窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(pattern,sentence)
    #['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡', '']
    print(sentence_list)

    while '' in sentence_list:
        sentence_list.remove('')
    ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
    print(sentence_list)
    
if __name__ == "__main__":
    main()