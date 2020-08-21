"""
exercise1:实现计算求最大公约数和最小公倍数的函数

Version : 0.1
Author  : 郑超轩
Date    : 2020/01/22
"""
def max_gys(m,n):
    if m > n:
        m,n = n,m
        
    for i in range(m,0,-1):
        if m % i ==0 and n % i == 0:
            return i

def min_gbs(m,n):
    i = max_gys(m,n)
    return m*n//i


def main():
    m = int(input('m = '))
    n = int(input('n = '))
    print('最大公约数为：%d' % (max_gys(m,n)))
    print('最小公倍数为：%d' % (min_gbs(m,n)))

if __name__ == '__main__':
    main()
