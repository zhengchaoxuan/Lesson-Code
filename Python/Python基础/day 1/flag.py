"""
用Python的turtle模块绘制国旗

"""
import turtle


def draw_rectangle(x,y,width,heigh):
    """绘制矩阵"""
    turtle.goto(x,y)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(heigh)
        turtle.left(90)
    turtle.end_fill()


def draw_star(x,y,radius):
    """绘制五角星"""
    turtle.setpos(x,y)
    pos1=turtle.pos()
    turtle.circle(-radius,72)
    pos2=turtle.pos()
    turtle.circle(-radius,72)
    pos3=turtle.pos()
    turtle.circle(-radius,72)
    pos4=turtle.pos()
    turtle.circle(-radius,72)   
    pos5=turtle.pos()
    turtle.color('yellow','yellow')
    turtle.begin_fill()
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()

    

def main():
    """主程序"""
    turtle.speed(3)
    turtle.penup()
    x,y=-270,-180
    #画国旗主体
    width,heigh=540,360
    draw_rectangle(x,y,width,heigh)

    #画大星星
    pice=22
    x_center,y_center=x+5*pice,y+heigh-5*pice
    turtle.goto(x_center,y_center)
    turtle.left(90)
    turtle.forward(3*pice)
    turtle.right(90)
    draw_star(turtle.xcor(),turtle.ycor(),3*pice)

    x_poses, y_poses = [8, 10, 10, 8], [2, 4, 7, 9]
    #画小星星
    for x_pos,y_pos in zip(x_poses,y_poses):
        turtle.goto(x + x_pos * pice, y + heigh - y_pos * pice)
        turtle.left(turtle.towards(x_center, y_center) - turtle.heading())
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)
    
    #隐藏海龟
    turtle.ht()

    #显示绘图窗口
    turtle.mainloop()

if  __name__=='__main__':
    main()


    