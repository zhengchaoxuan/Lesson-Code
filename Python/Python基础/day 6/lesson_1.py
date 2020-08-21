"""
lesson1:8个苹果分成四组每组至少一个苹果有多少种方案

Version : 0.1
Author  : 郑超轩
Data    : 2020/01/21
"""
#含有三个重复的循环语句，而“代码有很多种坏味道，重复是最坏的一种！”
M = int(input('M = '))
N = int(input('N = '))
sum_numerator = 1
sum_denumerator = 1
for i in range(1,M+1):
    sum_numerator = i*sum_numerator

for i in range (1,N+1):
    sum_denumerator = i*sum_denumerator
for i in range(1,M-N+1):
    sum_denumerator = i *sum_denumerator
print(sum_numerator/sum_denumerator)

#Version : 0.2 ---增加了函数，进行避免重复

def factorial(num):
    result = 1
    for i in range(1,num+1):
        result = i * result
    return result 


M1 = int(input('M = '))
N1 = int(input('N = '))
print(factorial(M)/(factorial(N)*factorial(M-N)))



