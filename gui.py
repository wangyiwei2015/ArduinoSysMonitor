import tkinter as tk
from tkinter import ttk

class Application:

    window = None
    box = None
    button = None

    def __init__(self, devices: list):
        self.window = tk.Tk()
        self.window.title('Select device')
        self.window.geometry("250x100")
        self.box = ttk.Combobox(self.window)
        self.box.pack()
        deviceList = devices
        # for i in range(len(devices)):
        #     deviceList[i] = str(i) + ' ' + devices[i]
        self.box['value'] = tuple(deviceList)
        self.box.current(0)
        self.button = ttk.Button(self.window,text='Connect',command=self.onConnectAction)
        self.button.pack()

    def onConnectAction(self):
        self.box.configure(state='disabled')
        self.button.configure(state='disabled')
        #self.callback(int(str(self.box.get()).split(' ')[0]))
        self.callback(str(self.box.get()))

    def callback(self,port: str):
        pass

    def start(self):
        self.window.mainloop()

class ErrorWindow:
    def __init__(self):
        window = tk.Tk()
        window.title('Error')
        window.geometry("250x100")
        text = ttk.Label(window, text='No available ports')
        text.pack()
        window.mainloop()

'''
from PyQt5 import QtGui, QtWidgets, QtCore

class Application:
    app = QtCore.QCoreApplication([])
    icon = QtGui.QIcon(fileName='icon.png')
    tray = QtWidgets.QSystemTrayIcon(icon=icon)
    rootMenu = QtWidgets.QMenu()
    deviceMenu = QtWidgets.QMenu(title='Select device')
    currentDevice = 0

    def __init__(self, deviceList: list):
        QtCore.QCoreApplication.setQuitOnLastWindowClosed(False)
        i = 1
        for item in deviceList:
            action = QtWidgets.QAction(text=item)
            action.triggered = lambda: self.onDeviceChanged(i)
            self.deviceMenu.addAction(action)
            i += 1
        self.rootMenu.addMenu(self.deviceMenu)
        exitAction = QtWidgets.QAction(text='&Exit')
        exitAction.triggered = self.quit()
        self.rootMenu.addAction(exitAction)
        self.tray.setContextMenu(self.rootMenu)
        self.tray.Trigger = self.onTrayClicked
        self.tray.show()

    def quit(self):
        QtCore.QCoreApplication.instance().quit()
        self.tray.setVisible(False)

    def onTrayClicked(self):
        pass

    def onDeviceChanged(self,newDevice: int):
        pass
    
'''