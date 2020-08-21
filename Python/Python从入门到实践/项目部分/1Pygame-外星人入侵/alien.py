'''加载外星人，并且设置外星人的位置'''

import pygame
from  pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_setting,screen):
        super().__init__()
        self.screen = screen
        self.ai_setting =ai_setting

        self.image = pygame.image.load('Python从入门到实践/项目部分/1Pygame-外星人入侵/image/alien.bmp')
        self.rect = self.image.get_rect()
        
        #把外星人首先放在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)     
    
    #判断是否到达边缘标志
    def check_edges(self):
        if self.rect.right>=self.ai_setting.screen_width:
            return True
        elif  self.rect.left<=0:
            return True
            
    def update(self):
        #error2:失败
        '''
        self.x += self.ai_setting.alien_xspeed
        self.rect.x = int(self.x)
        '''
        self.rect.x += self.ai_setting.alien_xspeed*self.ai_setting.alien_xdiction


    def draw_alien(self):
        self.screen.blit(self.image,self.rect)