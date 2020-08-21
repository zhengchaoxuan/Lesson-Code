'''增加按钮部分'''
import pygame
from pygame import font
class Botton(object):
    def __init__(self,ai_settings,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 100
        self.height = 60

        self.color = [0,255,0]
        self.fontcolor = [255,255,255]
        
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        
        self.font = font.SysFont(None,38) #从系统字体库创建一个 Font 对象字体：默认，size:48

        self.prep_msg(msg)
    
    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.fontcolor,self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.color,self.rect) #绘制一个用颜色填充的按键
        self.screen.blit(self.msg_image,self.msg_image_rect)



