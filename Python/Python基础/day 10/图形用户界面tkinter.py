"""
lesson1 : 使用tkinter做一个简单的GUI应用

Version : 0.1
Author  : 郑超轩
Date    : 2020/02/15
"""
"""导入tkinter模块"""
import tkinter
import tkinter.messagebox

def main():
    flag = True
    # 修改标签上的文字
    def change_label_text():
        nonlocal  flag 
        flag = not flag #保证的是和原意思
        color ,msg = ('red','Hello,world!') if flag else ('blue','Goodbye,world!')
        label.config(text = msg,fg = color) #text,fg
    
    #确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示','确定要退出吗?'):
            top.quit() #top是顶层窗口对象
    
    #创建顶层窗口
    top = tkinter.Tk() #k小写
    #设计窗口大小
    top.geometry('240x160') #不能用*
    #设计窗口标题
    top.title('小游戏')
    #创建标签对象并条添加到顶层窗口(内容，字体，颜色)
    label = tkinter.Label(top,text='Hello,world!',font = 'Arial -32',fg = 'red')
    label.pack(expand = 1) #不理解 #expand置1 使能fill属性
    #创建一个装按钮的容器
    panel = tkinter.Frame(top)
    #创建按钮对象 指定添加到那个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel,text = '修改',command = change_label_text)
    button1.pack(side ='left')
    button2 = tkinter.Button(panel,text = '退出',command = confirm_to_quit)
    button2.pack(side = 'right')
    #panel.pack(side = 'bottom') --- 没有的话不显示
    #开启主事件循环
    tkinter.mainloop()


if __name__ =="__main__":
    main()
