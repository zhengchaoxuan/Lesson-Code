'''加载飞船，并且设置飞船的位置'''
import pygame 
from pygame.sprite import Sprite  
class Ship(Sprite):
    '''属性：包括把屏幕和图像转换成矩形处理'''
    def __init__(self,screen,ai_settings):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('Python从入门到实践/项目部分/1Pygame-外星人入侵/image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #在飞船的属性center存储小数值
        self.center = float(self.screen_rect.centerx)

        #计算屏幕的宽和飞船的中心，其相减可以保证飞船不离开屏幕
        self.ai_settings = ai_settings
        self.default_centerx = self.rect.centerx
    
        # 把飞船放入屏幕底部的中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #表示飞船不离开屏幕
        #进行描述飞船停止
        self.move_right = False
        self.move_left = False
        
    
    def update(self):
        if self.move_right and self.rect.centerx<= self.ai_settings.screen_width -self.default_centerx:
            self.center += self.ai_settings.ship_speed
        if self.move_left and self.rect.centerx>=0+self.default_centerx:
            self.center -= self.ai_settings.ship_speed
        
        #只存储整数部分
        self.rect.centerx = self.center

    
    def ship_center(self):
        self.center = self.screen_rect.centerx

    #进行定点绘制
    def blitme(self):
        self.screen.blit(self.image,self.rect)