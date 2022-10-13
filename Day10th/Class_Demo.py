class Student:
    def getData(self,fname,lname):
        self.f=fname
        self.l=lname
    def putData(self):
        print("First Name:",self.f)
        print("Lats Name:",self.l)

sdata=Student()
FirstN=input("Enter Your First name:")
LastN=input("Enter Your Lats name:")
sdata.getData(FirstN,LastN)
sdata.putData()

