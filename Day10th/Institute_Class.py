class Institute:
    def Personaldetails(self,fname,lname,city,age,qualification):
        self.f=fname
        self.l=lname
        self.city=city
        self.age=age
        self.qualitfi=qualification
        print("Hello",self.f,"Your City is",self.city,"Age is",self.age,"and your Qualification is",self.qualitfi)
    def Course(self):
        while True:
            print("*" * 40)
            print("1. Python")
            print("2. Java")
            print("3. PHP")
            print("4. C")
            print("5. Web design")
            print("6. Exit")
            print("*" * 40)
            Choice = int(input("Enter Your Choice:"))

            if Choice == 1:
                Coursh_fee = "Rs.30000/-"
                print("Your Selected Course Fee is", Coursh_fee)
                while True:
                    print("*" * 40)
                    print("1. Yes")
                    print("2. No")
                    print("3. Exit")
                    print("*" * 40)
                    choice = int(input("Enter Choice:"))
                    if choice==1:
                        print("Thank you for Choosing our Course.","\nWelcome to Tpos Institute")
                        print("Our Team will be Connect you within 5 hours")
                        #url='https://google.com'
                        #webbrowser.get('C:\Program Files\Google\Chrome\Application\chrome.exe %s').open(url)
                        break
                    elif choice==2:
                        print("Thank you")
                    else:
                        print("Thank You")
                        break
            elif Choice == 2:
                Coursh_fee = "Rs.40000/-"
                print("Your Selected Course Fee is", Coursh_fee)
                while True:
                    print("*" * 40)
                    print("1. Yes")
                    print("2. No")
                    print("3. Exit")
                    print("*" * 40)
                    choice = int(input("Enter Choice:"))
                    if choice==1:
                        print("Thank you for Choosing our Course.","\nWelcome to Tpos Institute")
                        print("Our Team will be Connect you within 5 hours")
                        break
                    elif choice==2:
                        print("Thank you")
                    else:
                        print("Thank You")
                        break
            elif Choice == 3:
                Coursh_fee = "Rs.20000/-"
                print("Your Selected Course Fee is", Coursh_fee)
                while True:
                    print("*" * 40)
                    print("1. Yes")
                    print("2. No")
                    print("3. Exit")
                    print("*" * 40)
                    choice = int(input("Enter Choice:"))
                    if choice==1:
                        print("Thank you for Choosing our Course.","\nWelcome to Tpos Institute")
                        print("Our Team will be Connect you within 5 hours")
                        break
                    elif choice==2:
                        print("Thank you")
                    else:
                        print("Thank You")
                        break
            elif Choice == 4:
                Coursh_fee = "Rs.15000/-"
                print("Your Selected Course Fee is", Coursh_fee)
                while True:
                    print("*" * 40)
                    print("1. Yes")
                    print("2. No")
                    print("3. Exit")
                    print("*" * 40)
                    choice = int(input("Enter Choice:"))
                    if choice==1:
                        print("Thank you for Choosing our Course.","\nWelcome to Tpos Institute")
                        print("Our Team will be Connect you within 5 hours")
                        break
                    elif choice==2:
                        print("Thank you")
                    else:
                        print("Thank You")
                        break
            elif Choice == 5:
                Coursh_fee = "Rs.35000/-"
                print("Your Selected Course Fee is", Coursh_fee)
                while True:
                    print("*" * 40)
                    print("1. Yes")
                    print("2. No")
                    print("3. Exit")
                    print("*" * 40)
                    choice = int(input("Enter Choice:"))
                    if choice==1:
                        print("Thank you for Choosing our Course.","\nWelcome to Tpos Institute")
                        print("Our Team will be Connect you within 5 hours")
                        break
                    elif choice==2:
                        print("Thank you")
                    else:
                        print("Thank You")
                        break
            else:
                print("Thank you for given your Time,\nIf you have any query Please call")
                break
    def Intersted(self):
        while True:
            print("*" * 40)
            print("1. Yes")
            print("2. No")
            print("3. Exit")
            print("*" * 40)
            choice=int(input("Enter Choice:"))



init=Institute()
Fname=input("Enter your First Name:")
Lname=input("Enter your last Name:")
City=input("Enter your CityName:")
Age=int(input("Enter Your Age:"))
Qualification=input("Enter Qualification:")
init.Personaldetails(Fname,Lname,City,Age,Qualification)
init.Course()



