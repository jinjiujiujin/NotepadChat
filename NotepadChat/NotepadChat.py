#使用记事本进行聊天

#notepad chat room
#@author : zyyz
#@latest update:2019/09/22

import os
import win32api

if __name__ == "__main__":
    #method1
    #启动服务端 覆盖掉本程序
    #os.system("python Server.py")
    #method2
    #打开一个文件
    win32api.ShellExecute(0, "open", "Server.py", '', '', 1)
    ##3个客户端
    win32api.ShellExecute(0, "open", "Client.py", '', '', 1)
    win32api.ShellExecute(0, "open", "Client.py", '', '', 1)
    win32api.ShellExecute(0, "open", "Client.py", '', '', 1)
    #win32api.ShellExecute(0, "open", "Notepad", '', '', 3)#打开记事本，并最大化