import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkmas
from time import sleep

class Application:
    window = None
    box = None
    button = None
    def __init__(self, devices: list):
        self.window = tk.Tk()
        self.window.title('端口选择')
        self.window.geometry("250x105")

        self.box = ttk.Combobox(self.window)
        self.box.pack(padx=40,pady=15)
        deviceList = devices
        self.box['value'] = tuple(deviceList)
        self.box.current(0)

        self.button = ttk.Button(self.window,
                                text='连接',
                                command=self.onConnectAction)
        self.button.pack(padx=40,pady=10)

    def onConnectAction(self):
        if(self.box.current()==0):
            self.errorWindow()
            return
        self.box.configure(state='disabled')
        self.button.configure(state='disabled')
        #self.window.state('icon')#最小化
        self.window.withdraw()#隐藏窗口
        self.callback(str(self.box.get()))

    def start(self):
        self.window.mainloop()
    
    def errorWindow(self):
        tkmas.showwarning("警告","请选择设备端口")
        return