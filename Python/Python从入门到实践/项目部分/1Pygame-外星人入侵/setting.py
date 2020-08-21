'''屏幕背景参数的设置'''
#version o.1
#1. 增加 限定子弹数量
class Setting(object):
    def __init__(self):

        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230,230,230)

        #飞船设置
        self.ship_speed = 1.5
        self.ship_number = 1

        # 外星人设置：左右移动的速度,向下的速度，表示相反的方向的标志
        self.alien_xspeed = 1
        self.alien_xdiction =1 #1表示右边，-1表示左边
        self.alien_yspeed = 5


        #子弹设置
        self.bullet_color = [60,60,60]
        self.bullet_speed = 1
        self.bullet_height = 15
        self.bullet_width  = 5
        self.bullet_number = 5

        #增加速度
        self.add_speed = 1

        #得分--消灭一个外星人得50分
        self.get_points = 50 

    #提升速度,同时增加得分
    def increase_allspeed(self):
        self.bullet_speed +=self.add_speed
        self.alien_yspeed +=self.add_speed
        self.ship_speed  += self.add_speed
        self.get_points = int(self.get_points*1.2)
    
        



        
    