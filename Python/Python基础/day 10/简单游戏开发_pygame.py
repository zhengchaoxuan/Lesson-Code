"""
lesson1 : 使用Pygame进行游戏开发--制作窗口
描述:理解面向对象程序设计的编程思路

Version : 0.1
AUthor  : 郑超轩
Date    : 2020/02/18

import pygame

def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()
"""

"""
lesson2 : 使用Pygame进行游戏开发--窗口绘图--draw
描述:理解面向对象程序设计的编程思路

Version : 0.1
AUthor  : 郑超轩
Date    : 2020/02/18

import pygame

def main():

    #初始化pyname
    pygame.init()
    #初始化窗口大小和标题
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    
    #2 设置窗口的背景色（BGR组成的元组）--fill
    screen.fill((242,242,242))

    #2 绘制一个圆（参数：screen,颜色，圆心位置，半径，0表示填充）
    pygame.draw.circle(screen,(255,0,0),(100,100),30,0)

    #2 刷新当前窗口
    pygame.display.flip() #不添加这个函数的话就只能等系统刷新

    running = True
    while running:
        for event in pygame.event.get():
            if event ==pygame.QUIT:
                running = false

if __name__ == '__main__':
    main()
"""


"""
lesson3 : 使用Pygame进行游戏开发--加载图像--image.load函数加载，和blit函数渲染
描述:理解面向对象程序设计的编程思路

Version : 0.1
AUthor  : 郑超轩
Date    : 2020/02/18

import pygame

def main():

    #初始化pyname
    pygame.init()
    #初始化窗口大小和标题
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    
    #2 设置窗口的背景色（BGR组成的元组）--fill
    screen.fill((242,242,242))

    #2 绘制一个圆（参数：screen,颜色，圆心位置，半径，0表示填充）
    #pygame.draw.circle(screen,(255,0,0),(100,100),30,0)

    #3 加载图片
    image = pygame.image.load("D:/图片/壁纸/动漫/7.jpg")
    
    #3 渲染图像
    screen.blit(image,(0,0)) #（0，0）位置
    
    #2 刷新当前窗口
    #pygame.display.flip() #不添加这个函数的话就只能等系统刷新

    running = True
    while running:
        for event in pygame.event.get():
            if event ==pygame.QUIT:
                running = false


if __name__ == '__main__':
    main()
"""


"""
lesson2 : 使用Pygame进行游戏开发--动画效果
描述:理解面向对象程序设计的编程思路

Version : 0.1
AUthor  : 郑超轩
Date    : 2020/02/18


import pygame

def main():

    #初始化pyname
    pygame.init()
    #初始化窗口大小和标题
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    running = True
    #4 x,y 代表球的位置
    x=50
    y=50

    while running:
        for event in pygame.event.get():
            if event ==pygame.QUIT:
                running = false
        screen.fill((255,255,255))
        pygame.draw.circle(screen,(255,0,0),(x,y),30,0)
        pygame.display.flip() #刷新
        #4 保存50ms 
        pygame.time.delay(50)
        x += 5
        y += 5


if __name__ == '__main__':
    main()
"""





