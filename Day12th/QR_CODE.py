import pyqrcode
from tkinter import *
import tkinter.messagebox as msg

def generateQR():
    inputString=enterTextFiled.get()
    scale=enterScaleFiled.get()
    if len(scale):
        try:
            scale=int(scale)
        except:
            msg.showerror("Error","Scale Should be integer value Ex:1,2,3,....")
            return
    else:
        scale=5
    if len(inputString):
        qrCode=pyqrcode.create(inputString)
        savePath="C:\\Users\\Vishal\\Desktop\\Tops_Assi\\OR_Image"+inputString+"_"+str(scale)
        qrCode.svg(savePath+".svg",scale=scale)
        #qrCode.png(savePath+".png",scale=scale)
        msg.showinfo("Success","Your QR Code is Generated and save at this path:"+savePath+".png/.svg")
    else:
        msg.showerror("Error","Text Filed is Empty")
def clearAll():
    enterTextFiled.delete(0,'end')
    enterTextFiled.focus_set()

if __name__=="__main__":
    windows=Tk()
    windows.configure(bg='light green')
    windows.geometry("600x100")
    windows.title("QR CODE GENERATOR")
    enterTextLable=Label(windows,text="Enter Text",fg="black",bg="grey")
    enterTextLable.grid(row=2,column=1,sticky="E",padx="10",pady="10")
    enterScaleLable=Label(windows,text="Enter Scale",fg="black",bg="grey")
    enterScaleLable.grid(row=2,column=4,sticky="E",padx="10",pady="10")
    enterTextFiled=Entry(windows)
    enterTextFiled.grid(row=2,column=2,sticky="E",ipadx="60",pady="10")
    enterScaleFiled=Entry(windows)
    enterScaleFiled.grid(row=2,column=5,sticky="E",pady="10")
    generationButton=Button(windows,text="Generate",bg="red",fg="black",command=generateQR)
    clearButton=Button(windows,text="Clear",bg="red",fg="black",command=clearAll)
    generationButton.grid(row=3,column=3)
    clearButton.grid(row=4,column=3,pady="5")
    windows.mainloop()