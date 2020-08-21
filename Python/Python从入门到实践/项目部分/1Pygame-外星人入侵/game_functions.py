##date:2020/07/21
# version:0.1
# update_evet:新增加 update_event 函数（其为重构）只设置按键 -- 用户按下关闭按钮，关闭（切没有关闭按钮）

#version:0.2
# 1.update_secreen:新增加 update_secreen 函数（其为重构），用于进行屏幕循环内的更新，包括屏幕颜色，飞船位置绘制，进行最近绘制屏幕可见
# 2.update_event:新增功能----按键（飞船向右）

#date: 2020/07/23
#1.重构函数update_bullets()：保证子弹从屏幕出去后就不保持再bullet上面
import sys
import os
import pygame
import json 
from bullet import Bullet
from alien import Alien
from time import sleep

def update_event(aliens,ai_settings,screen,bullets,ship,status,bottons):

    for event in pygame.event.get():
        #键盘按下
        if event ==pygame.QUIT:
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            """描述飞船控制"""
            if event.key == pygame.K_RIGHT:
                ship.move_right = True
            if event.key ==pygame.K_LEFT:
                ship.move_left = True

            """描述子弹控制"""
            if event.key == pygame.K_SPACE:
                if len(bullets)<ai_settings.bullet_number:
                    new_bullet =Bullet(screen,ai_settings,ship)
                    bullets.add(new_bullet)

            ''' 程序重置，重新开始和暂停'''    
            if event.key == pygame.K_r:
                status.game_active = False
            if event.key == pygame.K_p:
                status.game_pause = True
            if event.key == pygame.K_a:
                status.game_pause = False
            

            if event.key == pygame.K_q: #用户按下q关闭按钮
                #进行把最高分数据存储到json文件中
                highscore_json = 'Python从入门到实践/项目部分/1Pygame-外星人入侵/highscore.json'
                with open( highscore_json,'w') as highscore_object:
                    json.dump(status.high_score,highscore_object)
                #sys.exit()的退出比较优雅，调用后会引发SystemExit异常，可以捕获此异常做清理工作
                sys.exit(0)
                #键盘放开
        elif event.type ==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            if event.key ==pygame.K_LEFT:
                ship.move_left =False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos() #获得位置
            #进行判断位置
            check_mouse_button(aliens,ai_settings,screen,bullets,ship,status,bottons,mouse_x,mouse_y) 


def update_screen(ai_settings,screen,ship,bullets,aliens,bottons,scores,status):
    screen.fill(ai_settings.screen_color)
    
    #进行计分
    scores.draw_score()

    #进行飞船绘制
    ship.blitme()

    #进行子弹的绘制
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.update()

    #进行外星人的绘制
    # 这使用源surface的Sprite.image属性和Sprite.rect的位置---要包含screen的blit
    aliens.draw(screen)

    if not status.game_active:
        #进行开始按键设置
        bottons.draw_button()
    
    #进行最近绘制屏幕可见
    pygame.display.flip()


def update_bullets(aliens,ai_settings,screen,ship,bullets,scores,status):
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)   
    bullets.update()
    check_bullet_alien_collide(aliens,ai_settings,screen,ship,bullets,scores,status)


def check_bullet_alien_collide(aliens,ai_settings,screen,ship,bullets,scores,status):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True) #创建一个字典
    if collisions: #只用这个只能保证一次碰撞会加50，不能保证子弹一次碰2个的情况
        for alien in collisions.values():
            status.score += ai_settings.get_points
            scores.prep_score()
        get_highscore(status,scores)
        
        
    #产生新的外星人群
    if len(aliens) == 0:
        bullets.empty() #清空子弹
        ai_settings.increase_allspeed() #增速
        status.level +=1
        scores.prep_level()
        create_aliens(aliens,ai_settings,screen,ship)

    
#把该函数进行重构，分为一个确定一行的外星人的个数,，一个确定位置的外星人，一个是确定一行创造外星人
# 确定一列数的外星人个数
def create_aliens_ynumber(ai_settings,screen,ship):
    #减去飞船和你想要预留的飞船下降的高度
    alien  = Alien(ai_settings,screen)
    alien_height = ai_settings.screen_height - ship.rect.height-3*alien.rect.width
    alien_yallnumber = int(alien_height/(2*alien.rect.height))
    return alien_yallnumber


#确定一行的外星人的个数
def create_aliens_xnumber(ai_settings,screen):
    #减少两边的宽度
    alien =Alien(ai_settings,screen)

    alien_width = ai_settings.screen_width - 2*alien.rect.width
    alien_xallnumber = int(alien_width/(2*alien.rect.width))
    return alien_xallnumber

# 创造一个确定位置的外星人
def create_xy_aliens(aliens,ai_settings,screen,alien_xnumber,alien_ynumber):
    alien =Alien(ai_settings,screen)
    alien.rect.x=alien.rect.width+2*alien.rect.width*alien_xnumber  #空一外星人的位置
    alien.rect.y = alien.rect.height+2*alien.rect.height*alien_ynumber
    aliens.add(alien)

#确定多行创造外星人
def create_aliens(aliens,ai_settings,screen,ship):
    alien =Alien(ai_settings,screen)
    alien_xallnumber = create_aliens_xnumber(ai_settings,screen)
    alien_yallnumber = create_aliens_ynumber(ai_settings,screen,ship)

    for alien_xnumber in range(alien_xallnumber):
        for alien_ynumber in range(alien_yallnumber):
            create_xy_aliens(aliens,ai_settings,screen,alien_xnumber,alien_ynumber)
    

# 外星人移动
def check_fleet_aliens(aliens,ai_settings):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_aliens(aliens,ai_settings)
            break

def change_fleet_aliens(aliens,ai_settings):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_yspeed
    ai_settings.alien_xdiction *=-1

def update_aliens(aliens,ai_settings,ship,bullets,screen,status,scores):
    check_fleet_aliens(aliens,ai_settings)
    aliens.update()

    # 检测外星人和飞船碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(aliens,ai_settings,ship,bullets,screen,status,scores)
    #检测外星人是否到达屏幕底
    alien_arrive_screenbottom(aliens,ai_settings,ship,bullets,screen,status,scores)    

# 碰撞后的处理方式
def ship_hit(aliens,ai_settings,ship,bullets,screen,status,scores):
    if  status.ship_left>0:     
        status.ship_left -= 1
        scores.prep_ship()
        #清空外星人，和飞船
        bullets.empty()
        aliens.empty()
        #创造外星人
        create_aliens(aliens,ai_settings,screen,ship)
        #把飞船转到屏幕中心
        ship.ship_center()
        #暂停
        sleep(0.5)
    else:
        #分数清零
        status.score = 0
        status.level = 1
        status.ship_left = ai_settings.ship_number 

        scores.prep_score()
        scores.prep_level()
        scores.prep_ship()
        status.game_active = False

def alien_arrive_screenbottom(aliens,ai_settings,ship,bullets,screen,status,scores):
    #判断一群外星人的一个外星人
    for alien in aliens.sprites():
        if alien.rect.bottom>= ai_settings.screen_height:
            ship_hit(aliens,ai_settings,ship,bullets,screen,status,scores)
            break


#进行按钮判断位置，
# 2.新增每次按按钮就进行游戏的重置    
# 3.增加隐藏光标       
def check_mouse_button(aliens,ai_settings,screen,bullets,ship,status,bottons,mouse_x,mouse_y):
    bottons_click = bottons.rect.collidepoint(mouse_x,mouse_y)
    if bottons_click and not status.game_active:
        #pygame.mouse.set_visible(False) #设置光标不可见
        
        status.ship_left = ai_settings.ship_number  #重置飞船个数

        
        status.game_active = True   

        #清空外星人，和飞船
        bullets.empty()
        aliens.empty()

        #创造外星人
        create_aliens(aliens,ai_settings,screen,ship)
        #把飞船转到屏幕中心
        ship.ship_center()  

#判断最高分
def get_highscore(status,scores):
    if status.high_score<=status.score:
        status.high_score = status.score
        scores.prep_highscore()
        
#获得json中的数据   
def get_jsonhighscore():
    try:
        highscore_json = 'Python从入门到实践/项目部分/1Pygame-外星人入侵/highscore.json'
        with open(highscore_json,'r') as highscore_object: 
            high_score = json.load(highscore_object)
            return high_score
    except FileNotFoundError:
        print('数据文件没有找到!') 
                   




        