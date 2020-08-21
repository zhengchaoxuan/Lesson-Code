# 第一个Python项目 --- 外星人入侵（Pygame）

# date ：2020/07/21
# version :0.1
# 问题1：为什么alien.draw_alien函数，其self.screen.blit(self.image,self.rect)，self.image可随意改参数名字
# 问题2：alien.update添加self.x相加再赋值会出现只出现一列外星人

#1.使用Group.draw函数进行外星人的绘制 ---- 这使用源surface的Sprite.image属性和Sprite.rect的位置---要包含screen的blit
#2.alien.py： 添加生成外星人群的函数，和进行重构6
#3.进行外星人的移动设置（settting.py(设置速度)，alien.py进行真实改变）
#4.game_functions模块 update_bullet函数：使用pygame.sprite.groupcollicode进行碰撞显示，以及进行一些简单的测试

import pygame
from pygame.sprite import Group
import json
from setting import Setting 
from ship import Ship
from alien import Alien 
import game_functions
from gamestatus import GameStatus
from botton import Botton
from gamestatus import Score

def alien():
    #初始化
    pygame.init()

    #进行屏幕的大小和颜色,标题
    pygame.display.set_caption('Alien Invation')
    ai_settings = Setting()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    status = GameStatus(ai_settings,game_functions.get_jsonhighscore())


    #创建分数牌
    scores = Score(ai_settings,screen,status)

    bottons = Botton(ai_settings,screen,'Playing')

    #生成一个飞船，一群子弹和外星人
    ship = Ship(screen,ai_settings)
    bullets = Group()  
    aliens = Group()
    #创造一群行星人
    game_functions.create_aliens(aliens,ai_settings,screen,ship)
    
    while(True):
        
        #进行响应鼠标和键盘
        game_functions.update_event(aliens,ai_settings,screen,bullets,ship,status,bottons)
        #键盘控制
        if status.game_active:

            if not status.game_pause:
            #跟新子弹，并删除消失在屏幕的子弹
                game_functions.update_bullets(aliens,ai_settings,screen,ship,bullets,scores,status)
                game_functions.update_aliens(aliens,ai_settings,ship,bullets,screen,status,scores)

        #更新屏幕
        game_functions.update_screen(ai_settings,screen,ship,bullets,aliens,bottons,scores,status)

alien1 = alien()