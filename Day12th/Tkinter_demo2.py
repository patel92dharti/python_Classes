from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def conn_sql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_interview_form")

def submit_button():
    if fnameB.get()=="" or mnameB.get()=="" or lnameB.get()=="" or AgeEn.get()=="" or AddE.get()=="" or Add2e.get()=="" or Addcity.get()=="" or Addstate.get()=="" or phonenumber.get()=="" or EmailE.get()=="":
        msg.showinfo("Submit Status", "All Fields Are Mandatory")
    else:
        conn=conn_sql()
        coursor=conn.cursor()
        query="insert into interview_form (first_name,mid_name,last_name,age,street_adress,street_adress1,city,state,phone_number,email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args=(fnameB.get(),mnameB.get(),lnameB.get(),AgeEn.get(),AddE.get(),Add2e.get(),Addcity.get(),Addstate.get(),phonenumber.get(),EmailE.get())
        coursor.execute(query,args)
        conn.commit()
        conn.close()
        fnameB.delete(0,'end')
        mnameB.delete(0,'end')
        lnameB.delete(0,'end')
        AgeEn.delete(0,'end')
        AddE.delete(0,'end')
        Add2e.delete(0,'end')
        Addcity.delete(0,'end')
        Addstate.delete(0,'end')
        phonenumber.delete(0,'end')
        EmailE.delete(0,'end')
        msg.showinfo("Submit Status","Data Submitted Successfully")

dharti=Tk()
dharti.geometry("550x1000")
dharti.resizable(width=False,height=False)
dharti.title("Online Interview Questionnaire Form")
dharti.configure(bg="#FFFFC1")


tital2=Label(dharti,text="Interview Questionnaire",font="Arial 20 bold",bg="#FFFFC1")
tital2.place(x=100,y=50)

details=Label(dharti,text="Personal Information:",font="Arial 10 bold",bg="#FFFFC1")
details.place(x=50,y=120)

fullname=Label(dharti,text="Full Name",font="Arial 10",bg="#FFFFC1")
fullname.place(x=50,y=150)

fnameB=Entry(dharti)
fnameB.place(x=50,y=180)
Fname=Label(dharti,text="First Name",font="Arial 8",bg="#FFFFC1")
Fname.place(x=50,y=200)

mnameB=Entry(dharti)
mnameB.place(x=180,y=180)
mname=Label(dharti,text="Middle Name",font="Arial 8",bg="#FFFFC1")
mname.place(x=180,y=200)

lnameB=Entry(dharti)
lnameB.place(x=310,y=180)
lname=Label(dharti,text="Last Name",font="Arial 8",bg="#FFFFC1")
lname.place(x=310,y=200)

age=Label(dharti,text="Age",font="Arial 10",bg="#FFFFC1")
age.place(x=50,y=230)
AgeEn=Entry(dharti)
AgeEn.place(x=50,y=260)

address=Label(dharti,text="Address",font="Arial 10",bg="#FFFFC1")
address.place(x=50,y=300)
AddE=Entry(dharti)
AddE.place(x=50,y=330)

#AddE.grid(row=4,column=1,ipadx)
streetAd=Label(dharti,text="Street Address",font="Arial 8",bg="#FFFFC1")
streetAd.place(x=50,y=350)

Add2e=Entry(dharti)
Add2e.place(x=50,y=380)
streetAd2=Label(dharti,text="Street Address Line 2",font="Arial 8",bg="#FFFFC1")
streetAd2.place(x=50,y=400)

Addcity=Entry(dharti)
Addcity.place(x=50,y=430)
city=Label(dharti,text="City",font="Arial 8",bg="#FFFFC1")
city.place(x=50,y=450)

Addstate=Entry(dharti)
Addstate.place(x=310,y=430)
state=Label(dharti,text="State / Province",font="Arial 8",bg="#FFFFC1")
state.place(x=310,y=450)


phonen=Label(dharti,text="Phone Number",font="Arial 10",bg="#FFFFC1")
phonen.place(x=50,y=490)
phonenumber=Entry(dharti)
phonenumber.place(x=50,y=520)

Email=Label(dharti,text="Email",font="Arial 10",bg="#FFFFC1")
Email.place(x=50,y=550)
EmailE=Entry(dharti)
EmailE.place(x=50,y=570)
EmailExam=Label(dharti,text="example@example.com",font="Arial 8",bg="#FFFFC1")
EmailExam.place(x=50,y=590)


submit=Button(dharti,text="Submit",bg="Green",fg="white",font="Arial 10",command=submit_button)
submit.place(x=50,y=630)



dharti.mainloop()