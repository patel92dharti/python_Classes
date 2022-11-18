class Shopping():
    def customer(self,cname,mobileno):
        self.cname=cname
        self.mobile=mobileno
        print("Hello,",self.cname,"Your Register Mobile Number is",self.mobile)
    def fashionCloth(self):
        while True:
            print("*" * 50)
            print("1.Men")
            print("2.Woman")
            print("3.Exit")
            print("*" * 50)

            choice=int(input("Enter the Choice: "))

            if choice==1:
                while True:
                    print("*"*50)
                    print("1.Jeans")
                    print("2.Shorts")
                    print("3.Sweater")
                    print("4.Jacket")
                    print("5.T-Shirt")
                    print("6.Shirt")
                    print("7.Suit")
                    print("8.Scarf")
                    print("9.Sock")
                    print("10.Tie")
                    print("11.Gloves")
                    print("12.Baseball Cap")
                    print("13.Belt")
                    print("14.Blazer")
                    print("15.Exit")
                    print("*"*50)

                    Choice=int(input("Enter the Choice: "))
                    print("*"*50)
                    if Choice==1:
                        print("Starting Price is Rs.1000/-")
                    elif Choice==2:
                        print("Starting Price is Rs.700/-")
                    elif Choice==3:
                        print("Starting Price is Rs.1500/-")
                    elif Choice==4:
                        print("Starting Price is Rs.1000/-")

                    elif Choice==5:
                        print("Starting Price is Rs.2500/-")

                    elif Choice==6:
                        print("Starting Price is Rs.2000/-")
                    elif Choice==7:
                        print("Starting Price is Rs.500/-")
                    elif Choice==8:
                        print("Starting Price is Rs.3500/-")
                    elif Choice==9:
                        print("Starting Price is Rs.1500/-")
                    elif Choice==10:
                        print("Starting Price is Rs.1500/-")
                    elif Choice==11:
                        print("Starting Price is Rs.1500/-")
                    elif Choice==12:
                        print("Starting Price is Rs.4500/-")
                    elif Choice==13:
                        print("Starting Price is Rs.1500/-")
                    elif Choice==14:
                        print("Starting Price is Rs.800/-")
                    else:
                        print("Thank You")
                        break

            if choice == 2:
                while True:
                    print("*" * 50)
                    print("1.Jeans")
                    print("2.Shorts")
                    print("3.Sweater")
                    print("4.Jacket")
                    print("5.T-Shirt")
                    print("6.Coat")
                    print("7.Boot")
                    print("8.Scarf")
                    print("9.Exit")
                    print("*" * 50)

                    Choice = int(input("Enter the Choice: "))
                    print("*" * 50)
                    if Choice == 1:
                        print("Starting Price is Rs.1000/-")
                    elif Choice == 2:
                        print("Starting Price is Rs.700/-")
                    elif Choice == 3:
                        print("Starting Price is Rs.1500/-")
                    elif Choice == 4:
                        print("Starting Price is Rs.1000/-")

                    elif Choice == 5:
                        print("Starting Price is Rs.2500/-")
                    elif Choice == 6:
                        print("Starting Price is Rs.2000/-")
                    elif Choice == 7:
                        print("Starting Price is Rs.500/-")
                    elif Choice == 8:
                        print("Starting Price is Rs.3500/-")

                    else:
                        print("Thank You")
                        break

    def electronic(self):
        while True:
            print("*"*50)
            print("1.Laptop")
            print("2.Computer")
            print("3.T.V")
            print("4.Washing Machine")
            print("5.Juicer")
            print("6.Robotic Vacume Cleaner")
            print("7.Laser Printer")
            print("8.Mobile")
            print("9.Refrigerator")
            print("10.Air Conditioner")
            print("11.Watch")
            print("12.WebCam")
            print("13.Toaster")

            print("14.Exit")
            choice=int(input("Enter the Choice Number: "))
            print("*" * 50)
            if choice==1:
                print("Starting Price is Rs.1000/-")

            elif choice==2:
                print("Starting Price is Rs.1000/-")

            elif choice==3:
                print("Starting Price is Rs.1000/-")

            elif choice==4:
                print("Starting Price is Rs.5000/-")
            elif choice==5:
                print("Starting Price is Rs.2000/-")
            elif choice==6:
                print("Starting Price is Rs.1000/-")

            elif choice==7:
                print("Starting Price is Rs.1000/-")
            elif choice==8:
                print("Starting Price is Rs.1000/-")
            elif choice==9:
                print("Starting Price is Rs.1000/-")
            elif choice==10:
                print("Starting Price is Rs.1000/-")
            elif choice==11:
                print("Starting Price is Rs.1000/-")
            elif choice==12:
                print("Starting Price is Rs.1000/-")

            elif choice==13:
                print("Starting Price is Rs.1000/-")
            else:
                print("Good Bye")
                break
shop=Shopping()
cname=input("Enter Your Name: ")
Mobile=int(input("Enter Your Mobile Number: "))
shop.customer(cname,Mobile)

while True:
    print("*"*50)
    print("1.Fashion Design")
    print("2.Electronics")
    print("3.Exit")
    print("*"*50)

    choice = int(input("Enter Your Choice:"))
    print("*"*50)
    if choice==1:
        shop.fashionCloth()
    elif choice==2:
        shop.electronic()
    else:
        print("Good Bye")
        break





