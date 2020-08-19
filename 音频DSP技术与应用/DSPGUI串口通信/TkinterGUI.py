
# project: 实现串口通信助手  -- 在别人代码基础上进行修改
# author :郑超轩
# date:2020/08/19
#流程：
# 1. 使用tkinter进行标签的编写
import tkinter
from tkinter import ttk
from SerialClass import SerialAchieve   # 导入串口通讯类

class Tkinter_GUI(object):
    def __init__(self):
        # 初始化窗体 -- 产生一个实例，添加标题和进行窗口设置
        self.mainwin = tkinter.Tk()
        self.mainwin.title("Dsp串口调试工具")
        self.mainwin.geometry("600x400")

        """使用LAbel进行文本内容，标签显示"""
        self.label1 = tkinter.Label(self.mainwin,text = "串口号:",font = ("宋体",12))
        self.label1.place(x = 5,y =5)
        self.label2 = tkinter.Label(self.mainwin, text="波特率:", font=("宋体", 12))
        self.label2.place(x=5, y=45)
        self.label3 = tkinter.Label(self.mainwin, text="校验位:", font=("宋体", 12))
        self.label3.place(x=5, y=85)
        self.label4 = tkinter.Label(self.mainwin, text="数据位:", font=("宋体", 12))
        self.label4.place(x=5, y=125)
        self.label5 = tkinter.Label(self.mainwin,text = "停止位:",font = ("宋体",12))
        self.label5.place(x = 5,y = 165)
        self.label6 = tkinter.Label(self.mainwin, text="发送数据内容:", font=("宋体", 12))
        self.label6.place(x=230, y=5)
        self.label7 = tkinter.Label(self.mainwin, text="接收数据内容:", font=("宋体", 12))
        self.label7.place(x=230, y=200)
        
        """使用 stringvar 和 ttk 下拉列表控件显示"""
        # 串口号 --通过获得串口值的值进行取值
        self.com1value = tkinter.StringVar()  # 窗体中自带的文本，创建一个值
        self.combobox_port = ttk.Combobox(self.mainwin, textvariable=self.com1value,width = 10,font = ("宋体",12))#初始化
        # values输入选定内容
        self.combobox_port["values"] = [""]  # 这里先选定
        self.combobox_port.place(x = 90,y = 5)  # 显示位置

        # 波特率
        self.bandvalue = tkinter.StringVar()  # 窗体中自带的文本，创建一个值
        self.combobox_band = ttk.Combobox(self.mainwin, textvariable=self.bandvalue, width=10, font=("宋体", 12)) 
        # 输入选定内容 
        self.combobox_band["values"] = ["4800","9600","14400","19200","38400","57600","115200"]  # 这里先选定
        self.combobox_band.current(1)  # 设置默认选中第6个
        self.combobox_band.place(x=90, y=45)  # 显示

        # 校验位
        self.checkvalue = tkinter.StringVar()  # 窗体中自带的文本，创建一个值
        self.combobox_check = ttk.Combobox(self.mainwin, textvariable=self.checkvalue, width=10, font=("宋体", 12))
        # 输入选定内容
        self.combobox_check["values"] = ["无校验位",'Odd','Even','Mark','Space']  # 这里先选定
        self.combobox_check.current(0)  # 默认选中第0个
        self.combobox_check.place(x=90, y=85)  # 显示

        # 数据位
        self.datavalue = tkinter.StringVar()  # 窗体中自带的文本，创建一个值
        self.combobox_data = ttk.Combobox(self.mainwin, textvariable=self.datavalue, width=10, font=("宋体", 12) )
        # 输入选定内容
        self.combobox_data["values"] = ["4", "5", "8",'9','16']  # 这里先选定
        self.combobox_data.current(0)  # 默认选中第0个
        self.combobox_data.place(x=90, y=125)  # 显示

        # 停止位
        self.stopvalue = tkinter.StringVar()  # 窗体中自带的文本，创建一个值
        self.combobox_stop = ttk.Combobox(self.mainwin, textvariable=self.stopvalue, width=10, font=("宋体", 12))
        # 输入选定内容
        self.combobox_stop["values"] = ['0',"1",'2']  # 这里先选定
        self.combobox_stop.current(0)  # 默认选中第0个
        self.combobox_stop.place(x=90, y=165)  # 显示
        
        # 发送的内容
        test_str = tkinter.StringVar(value="Hello,world")
        self.entrySend = tkinter.Entry(self.mainwin, width=13, textvariable=test_str, font=("宋体", 12))
        self.entrySend.place(x=80, y=260)  # 显示

        """ 显示框 """
        # 实现记事本的功能组件
        self.SendDataView = tkinter.Text(self.mainwin,width = 40,height = 9,font = ("宋体",13))  # text实际上是一个文本编辑器
        self.SendDataView.place(x = 230,y = 35)  # 显示

        self.ReceDataView = tkinter.Text(self.mainwin, width=40, height=9,font=("宋体", 13))  # text实际上是一个文本编辑器
        self.ReceDataView.place(x=230, y=230)  # 显示

class MainSerial(Tkinter_GUI):
    def __init__(self):
        super().__init__()

        # 定义串口变量
        self.port = None
        self.band = None
        self.check = None
        self.data = None
        self.stop = None
        self.myserial = None
        
        # 获取窗口的参数
        self.band = self.combobox_band.get()
        self.check = self.combobox_check.get()
        self.data = self.combobox_data.get()
        self.stop = self.combobox_stop.get()

        #进行赋值
        self.myserial = SerialAchieve(int(self.band),self.check,self.data,self.stop)

        # 处理串口值
        self.port_list = self.myserial.get_port()
        port_str_list = []  # 用来存储切割好的串口号
        for i in range(len(self.port_list)):
            # 将串口号切割出来, 以空格为分隔符
            lines = str(self.port_list[i])
            print(lines)
            str_list = lines.split(" ")
            port_str_list.append(str_list[0])
        self.combobox_port["values"] = port_str_list
        self.combobox_port.current(0)  # 默认选中第0个

        # 按键显示，打开串口，当按下标题标签时进行调用的回调函数：button_OK_click
        self.button_OK = tkinter.Button(self.mainwin, text="打开串口",
                                        command=self.button_OK_click, font = ("宋体",12),
                                        width = 10,height = 1)
        self.button_OK.place(x = 5,y = 210)  # 显示控件
        # 关闭串口,当按下标题标签时进行调用的回调函数：button_Cancel_click

        self.button_Cancel = tkinter.Button(self.mainwin, text="关闭串口",  # 显示文本
                                 command=self.button_Cancel_click, font = ("宋体",12),
                                 width=10, height=1)
        self.button_Cancel.place(x = 120,y = 210)  # 显示控件

        # 清除发送数据,当按下标题标签时进行调用的回调函数：button_clcSend_click
        self.button_Cancel = tkinter.Button(self.mainwin, text="清除发送数据",  # 显示文本
                                            command=self.button_clcSend_click, font=("宋体", 12),
                                            width=13, height=1)
        self.button_Cancel.place(x=400, y=2)  # 显示控件

        # 清除接收数据,当按下标题标签时进行调用的回调函数：button_clcRece_click
        self.button_Cancel = tkinter.Button(self.mainwin, text="清除接收数据",  # 显示文本
                                            command=self.button_clcRece_click, font=("宋体", 12),
                                            width=13, height=1)
        self.button_Cancel.place(x=400, y=197)  # 显示控件

        # 发送按键,当按下标题标签时进行调用的回调函数：button_Send_click
        self.button_Send = tkinter.Button(self.mainwin, text="发送",  # 显示文本
                                            command=self.button_Send_click, font=("宋体", 12),
                                            width=6, height=1)
        self.button_Send.place(x=5, y=255)  # 显示控件

        # 接收按键,当按下标题标签时进行调用的回调函数：button_Rece_click
        self.button_Send = tkinter.Button(self.mainwin, text="接收",  # 显示文本
                                          command=self.button_Rece_click, font=("宋体", 12),
                                          width=6, height=1)
        self.button_Send.place(x=5, y=310)  # 显示控件

    def show(self):
        self.mainwin.mainloop()

    def button_OK_click(self):
        '''
        @ 串口打开函数
        :return: 
        '''
        #没有使用到串口
        if self.port == None or self.myserial.port.isOpen() == False:
            self.myserial.open_port(self.combobox_port.get())

            print("打开串口成功")
        else:
            pass

    def button_Cancel_click(self):
        self.myserial.delete_port()
        print("关闭串口成功")

    def button_clcSend_click(self):
        self.SendDataView.delete("1.0","end")

    def button_clcRece_click(self):
        self.ReceDataView.delete("1.0", "end")

    def button_Send_click(self):
        try:

            if self.myserial.port.isOpen() == True:
                print("开始发送数据")
                send_str1 = self.entrySend.get()
                print(type(send_str1),send_str1)
                self.myserial.Write_data(send_str1)
                self.SendDataView.insert(tkinter.INSERT, send_str1+" ")
                print("发送数据成功")
            else:
                print("串口没有打开")
        except:
            print("发送失败")

    def button_Rece_click(self):
        try:
            readstr = self.myserial.Read_data()
            self.ReceDataView.insert(tkinter.INSERT, readstr + " ")
        except:
            print("读取失败")


if __name__ == '__main__':
    my_ser1 = MainSerial()
    my_ser1.show()