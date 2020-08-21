'''进行游戏统计跟踪---飞船还剩多少个，外星人消灭多少个'''
import pygame
from pygame import font
from pygame.sprite import Group
from ship import Ship

class GameStatus(object):
    def __init__(self,ai_settings,default_high_score):
        self.ai_settings = ai_settings
        self.ship_left = self.ai_settings.ship_number
        self.game_active =False
        self.game_pause = False

        #计分系统
        self.score = 0
        self.high_score = default_high_score #最高得分

        #显示等级(因为每次清空外星人群就会增速)
        self.level = 1 #默认为1

#显示分数
class Score():
    def __init__(self,ai_settings,screen,status):
        self.ai_settings  = ai_settings
        self.screen = screen
        self.status = status
        self.screen_rect = self.screen.get_rect()

        self.text_color = [30,30,30]
        self.font = font.SysFont(None,38)

        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ship()
    
    def prep_score(self):
        round_scores = int(round(self.status.score,-1)) #10位数
        score_str = "{:,}".format(round_scores)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.screen_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right-20
        self.score_image_rect.top = 20
    
    def prep_highscore(self):
        round_scores = int(round(self.status.high_score,-1)) #10位数
        score_str = "{:,}".format(round_scores)
        self.highscore_image = self.font.render(score_str,True,self.text_color,self.ai_settings.screen_color)
        self.highscore_image_rect = self.highscore_image.get_rect()
        self.highscore_image_rect.right = self.screen_rect.centerx-20
        self.highscore_image_rect.top = 20

    def prep_level(self):
        level_str = str(self.status.level)
        self.levelscore_image = self.font.render(level_str,True,self.text_color,self.ai_settings.screen_color)
        self.levelscore_image_rect = self.levelscore_image.get_rect()
        self.levelscore_image_rect.right = self.screen_rect.right-20
        self.levelscore_image_rect.top = self.score_image_rect.top + 30
    
    def prep_ship(self):
        self.ships = Group()
        for ship_leftnumber in range(self.status.ship_left):
            ship = Ship(self.screen,self.ai_settings)
            ship.rect.top = 10
            ship.rect.left= self.screen_rect.left+ ship_leftnumber*ship.rect.width
            self.ships.add(ship)

    def draw_score(self):
        self.screen.blit(self.score_image,self.score_image_rect)
        self.screen.blit(self.highscore_image,self.highscore_image_rect)
        self.screen.blit(self.levelscore_image,self.levelscore_image_rect)
        self.ships.draw(self.screen)

        
         


    