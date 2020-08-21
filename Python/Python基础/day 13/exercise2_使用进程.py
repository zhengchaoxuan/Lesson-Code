'''
exercise: 使用进程
描述：
1）使用run函数进行进程管理

Author  : 郑超轩
Date    : 2020.02.28
'''
from time import sleep
import tkinter
from tkinter import messagebox
from threading import   Thread

def main():

    class Downloadtask(Thread):
        def run(self):
            sleep(10)
            tkinter.messagebox.showinfo('提示','下载成功')
            button1.config(state = tkinter.NORMAL)

    def show_massage():
        tkinter.messagebox.showinfo('提示','作者：郑超轩（0.1version）')
        
    def task_run():
        #禁止按键
        button1.config(state = tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        Downloadtask(daemon=True).start()
        
            
    

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