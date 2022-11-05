#Apply for jOB in Company
class company():
    def company(self):
        print("*"*60)
        print("Welcome to the Our Company")
        print("*"*60)
    def empployee(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
        print("Your name is ",self.fname,self.lname,",And Age is ",self.age)
class qualification(company):
    def quli(self):
        while True:
            print("*" * 60)
            print("1. B-Com")
            print("2. BCA")
            print("3. M-com")
            print("4. MCA")
            print("5. B-tech")
            print("6. BSC_IT")
            print("7. BE")
            print("8. 10/12 PASS")
            print("9. Exit")
            print("*" * 60)

            choice = int(input("Choose the your Qualification:-"))

            if choice == 1:
                print("You are Eligible for Charted Accounted")
                print("*" * 60)
                com.B_Com()
                break
            elif choice == 2:
                print("You are Eligible for Software Engineer")
                print("*" * 60)
                com.BCA()
                break

            elif choice == 3:
                print("You are Eligible for Charted Accounted Manager")
                print("*" * 60)
                com.M_com()
                break
            elif choice == 4:
                print("You are Eligible for Sr.Software Engineer")
                print("*" * 60)
                com.MCA()
                break
            elif choice == 5:
                print("You are Eligible for Data science_Engineer")
                print("*" * 60)
                com.B_tech()
                break
            elif choice == 6:
                print("You are Eligible for Server/Network Engineer")
                print("*" * 60)
                com.BSC_IT()
                break
            elif choice == 7:
                print("you have to come for interview")
                print("*" * 60)
                com.BE()
                break
            elif choice == 8:
                print("Sorry for that , you are not eligible.")
                print("*" * 60)
                break
            elif choice == 9:
                print("Good Bye")
                print("*" * 60)
                break
            else:
                print("Please choose your option again!")
                print("*" * 60)
                continue

class salary(qualification):
    def B_Com(self):
        print("Your salary is Rs.30,000/-per Month to Rs.35,000/-per month")
        print("*" * 60)
        com.Choice_Option()
    def BCA(self):
        print("Your salary is Rs.30,000/-per Month to Rs.40,000/-per month")
        print("*" * 60)
        com.Choice_Option()

    def M_com(self):
        print("Your salary is Rs.50,000/-per Month to Rs.90,000/-per month")
        print("*" * 60)
        com.Choice_Option()

    def MCA(self):
        print("Your salary is Rs.60,000/-per Month to Rs.1,00,000/-per month")
        print("*" * 60)
        com.Choice_Option()

    def B_tech(self):
        print("Your salary is Rs.45,000/-per Month to Rs.65,000/-per month")
        print("*" * 60)
        com.Choice_Option()

    def BSC_IT(self):
        print("Your salary is Rs.60,000/-per Month to Rs.65,000/-per month")
        print("*" * 60)
        com.Choice_Option()

    def BE(self):
        print("Your salary is Rs.23000/-per Month to Rs.32000/-per month")
        print("*" * 60)
        com.Choice_Option()

class Choice(salary):
    def Choice_Option(self):
        while True:
            print("*" * 60)
            print("1. Yes")
            print("2. No")
            print("*" * 60)
            Choice1=int(input("You are interested/Not interested with our Company select your Choice: "))
            if Choice1==1:
                print("Please share your Document on Mail:-hr@test.com")
                break
            elif Choice1==2:
                print("Good Bye")
                break

com=Choice()
com.company()
Fname=input("Enter the First Name:")
Lname=input("Enter the Last Name:")
Age=int(input("Enter the Age:"))
com.empployee(Fname,Lname,Age)
com.quli()
