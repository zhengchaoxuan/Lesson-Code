"""
lesson1 : JSON文件

Version : 0.1
Auther  : 郑超轩
"""
import json 

def main():
    mydict = {
        'name'  : '郑超轩',
        'age'   : 21      ,
        'gender': '男'    ,
        'friends':['吴其达','other'],
        'cars' : [ 
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
            ]
    }
    try:
        with open('D:\Vistual studio editor\Code\python\day 11\date.json','w',encoding='utf-8') as f:
            json.dump(mydict,f)
    except IOError as e:
        print(e)
    print('保存数据完成！')

if __name__ =='__main__':
    main()

