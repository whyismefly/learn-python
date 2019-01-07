#!usr/bin/python
# encoding:utf-8
import time, sys

# 判断python的版本然后import对应的模块
if sys.version < '3':
    from Tkinter import *
else:
    from tkinter import *

mydelaymin = 0.01  # 窗口提示的延迟时间，以分钟计


# ------------------def-------------------
def showMessage():
    # show reminder message window
    root = Tk()  # 建立根窗口
    root.minsize(500, 200)   #定义窗口的大小
    # root.maxsize(1000, 400)  #不过定义窗口这个功能我没有使用
    root.withdraw()  # hide window
    # 获取屏幕的宽度和高度，并且在高度上考虑到底部的任务栏，为了是弹出的窗口在屏幕中间
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight() - 100
    # root.resizable(False, False)
    root.resizable(TRUE, TRUE)
    # 添加组件
    root.title("日常提示")
    frame = Frame(root, relief=RIDGE, borderwidth=3)
    frame.pack(fill=BOTH, expand=1)  # pack() 放置组件若没有则组件不会显示
    # 窗口显示的文字、并设置字体、字号
    label = Label(frame, text="提示一：",font="Monotype\ Corsiva -20 bold")
    label.pack(fill=BOTH, expand=1)
    # 按钮的设置
    button = Button(frame, text="OK", font="Cooper -25 bold", fg="red", command=root.destroy)
    button1 = Button(frame, text="完成", font="Cooper -25 bold", fg="red", command=root.attributes)

    button.pack(side=BOTTOM)
    button1.pack(side=BOTTOM)

    root.update_idletasks()
    root.deiconify()  # now the window size was calculated
    root.withdraw()  # hide the window again 防止窗口出现被拖动的感觉 具体原理未知？
    root.geometry('%sx%s+%s+%s' % (root.winfo_width() + 10, root.winfo_height() + 10,
                                   (screenwidth - root.winfo_width()) / 2, (screenheight - root.winfo_height()) / 2))
    root.deiconify()
    root.mainloop()
# showMessage()



def change_info():
    root = Tk()  # 建立根窗口
    frame = Frame(root, relief=RIDGE, borderwidth=3)
    label=label = Label(frame, text="11111111111：",font="Monotype\ Corsiva -20 bold")

while True:
    time.sleep(mydelaymin * 60)  # 参数为秒
    showMessage()
    # openWindow()
    change_info()