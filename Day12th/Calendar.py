from tkinter import *
import calendar

def showCalendar():
    cal=Tk()
    cal.config(bg="grey")
    cal.title("Calender for the Year")
    cal.geometry("550x600")
    year=int(year_filed.get())
    cal_content=calendar.calendar(year)
    calYear=Label(cal,text=cal_content,bg="#FFFFA0",font="consolas 10 bold")
    calYear.grid(row=5,column=1,padx=20)
    cal.mainloop()


if __name__=='__main__':
    root=Tk()
    root.configure(bg="#FFFFC0")
    root.geometry("250x140")
    root.title("Calender")
    cal=Label(root,text="Calender",bg="#8787CE",font=("times",28,"bold"))
    year=Label(root,text="Enter Year",bg="dark grey")
    year_filed=Entry(root)
    button=Button(root,text="Show Calender",bg="Green",fg="Black",command=showCalendar)

    #putting widgets in position
    cal.grid(row=1,column=1)
    year.grid(row=2,column=1)
    year_filed.grid(row=3,column=1)
    button.grid(row=4,column=1)

    root.mainloop()