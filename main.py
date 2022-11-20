from tkinter import *
import time
import os

os.system('cls')

angka =0
win = Tk()
frame = Frame(win,background="#006EB3")
frame.place(relx = 0.5,
                rely = 0.5,
                anchor = 'center')

win.geometry("1800x1800")
win.config(bg='#006EB3')
text1 = Label(frame,text=":(",font=("calibri",80),foreground="white",background="#006EB3")
text = Label(frame,text=f"Your pc ran into a problem and needs restart. We're just", font=("arial",20),background="#006EB3",foreground="white")
text2 = Label(frame,text=f"collecting some error info. And then we'll restart for you.\n", font=("arial",20),background="#006EB3",foreground="white")
text3 = Label(frame,text=f"{angka}% complete\n", font=("arial",20),background="#006EB3",foreground="white")
text4 = Label(frame,text="      ||         ||       For more information about this issue and possible fixies, visit", font=("arial",15),background="#006EB3",foreground="white")
text5 = Label(frame,text="                          https://youtu.be/xvFZjo5PgG0\n", font=("arial",15),background="#006EB3",foreground="white")
text6 = Label(frame,text="      \______/       If you call a support person, give them this info:", font=("arial",15),background="#006EB3",foreground="white")
text7 = Label(frame,text="                          Stop code: NEVER_GONNA_GIVE_YOU_UP", font=("arial",15),background="#006EB3",foreground="white")
text1.grid(row=0,column=0,sticky=W)
text.grid(row=1,column=0,sticky=W)
text2.grid(row=2,column=0,sticky=W)
text3.grid(row=3,column=0,sticky=W)
text4.grid(row=4,column=0,sticky=W)
text5.grid(row=5,column=0,sticky=W)
text6.grid(row=6,column=0,sticky=W)
text7.grid(row=7,column=0,sticky=W)

win.attributes('-fullscreen', True)
win.mainloop()
