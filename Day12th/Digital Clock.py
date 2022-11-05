from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("Dharti Patel Clockitty clock")
def time():
    string=strftime("%H:%M:%S: %p")
    lable.config(text=string)
    lable.after(1000,time)
lable=Label(root,font=("ds-digital",100),background="black",foreground="Green")
lable.pack()
time()
mainloop()