
"""
lesson 1 :exercise1_不使用进程
注意：
1）当点击“下载”按钮后整个程序的其他部分都被这个耗时间的任务阻塞而无法执行了，这显然是非常糟糕的用户体验
Author : 郑超轩
Date   : 2020.02.26
"""
from time import sleep
import tkinter
from tkinter import messagebox

def main():
    
    def task_run():
        sleep(10)
        tkinter.messagebox.showinfo('提示','下载成功')
    
    def show_massage():
        tkinter.messagebox.showinfo('提示','作者：郑超轩（0.1Version）')
    
    #创建窗口对象，进行窗口的描述：标题，大小，置顶
    top = tkinter.Tk() 
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost',1)

    #进行控件的设置
    panal = tkinter.Frame(top)
    button1 = tkinter.Button(panal,text='下载',command = task_run)
    button2 = tkinter.Button(panal,text='信息',command = show_massage)
    button1.pack(side='left')
    button2.pack(side='right')
    panal.pack(side='bottom')

    tkinter.mainloop()
    


if __name__ == '__main__':
    main()