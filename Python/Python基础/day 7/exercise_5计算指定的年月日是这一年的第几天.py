"""
exercise5:计算指定的年月日是这一年的第几天
设计逻辑：年判断是否为闰年，月的话每月的日期都不同，用元组表示

Version : 0.1
Author  : 郑超轩
Date    : 2020/02/11
"""
"""
param:
    year :年
    month:月
    day  :日
return:
    date:该年第几天
"""

def get_date(year,month,day):
    if year%4 ==0 and year%100!=0 or year%400==0 : 
        months =(31,28,31,30,31,30,31,31,30,31,30,31) #每月的天数
    else:
        months =(31,29,31,30,31,30,31,31,30,31,30,31) #每月的天数
    date = day
    for i in range(month-1):
        date+=months[i]
    return date

def main():
    print(get_date(2016,1,8))
    print(get_date(2018,12,3))
    
if __name__ =='__main__':
    main()

"""
参考答案：
判断闰年
def  is_leap_year(year):
    return year%4==0 and year%100!=0 or year%400==0:

计算日期
def which_day(year,month,date):
       days_of_month = [
            [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ][is_leap_year(year)]
        total = 0
        for index in range(month - 1):
            total += days_of_month[index]
        return total + date
"""