"""
exercise6 : 打印杨辉三角形(看完参考答案后，下午自己再做一次)
设计逻辑：
1）知道行数，列数等于n
2）保证第一个和最后一个是1
3）保证相加
Version : 0.1
Author  : 郑超轩
Date    : 2020/02/11
"""
def YH_triangle(rows):
    """
    杨辉三角形输出
    :param rows :输入的列数
    
    """
    yh = [[]] * rows  
    for i in range(len(yh)):
        yh[i] =[None]*(i+1)
        for j in range(len(yh[i])):
            if j==0 or j==i:
                yh[i][j]=1
            else:
                yh[i][j]=yh[i-1][j]+yh[i-1][j-1]
            print(yh[i][j],end='\t')
        print()
        

def main():
    rows = int(input('请输入rows:'))
    YH_triangle(rows)


if  __name__ =='__main__':
    main()

"""
input不加int类型：TypeError: can't multiply sequence by non-int of type 'str'
