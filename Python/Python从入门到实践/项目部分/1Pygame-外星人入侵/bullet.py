'''描述关于飞船子弹的部分'''
import pygame
from pygame.sprite  import Sprite

class Bullet(Sprite):
    
    def __init__(self,screen,ai_settings,ship):
        """创建一个子弹"""
        super().__init__()  #继承Sprite
        self.screen = screen

        self.bullet_color = ai_settings.bullet_color #颜色
        self.bullet_speed = ai_settings.bullet_speed #速度
        #创建一个位置在(0,0)矩形作为子弹，，之后再设置到正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储用小数表示的子弹位置,要表示速度
        self.y = float(self.rect.y)

    def update(self):
        '''描述子弹射出'''
        self.y-=self.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.bullet_color,self.rect)



