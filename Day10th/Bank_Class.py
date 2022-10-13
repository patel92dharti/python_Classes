class Bank:
    def openAccount(self,acnumber,acname,balance):
        self.acnumber=acnumber
        self.acname=acname
        self.balance=balance
        print("Hello",acname,"Your Account Number",self.acnumber,"your balance AMount is",self.balance,"Rs.")
    def Deposit(self,Amount):
        self.balance=self.balance+Amount

    def Withdraw(self,Amount):
        if Amount<=self.balance:
            self.balance=self.balance-Amount
        else:
            self.need=Amount-self.balance
            print("Sorry you need Another",self.need,"Rs.")
    def Checkbalance(self):
        print("Current Balance:",self.balance)

bank1=Bank()
Acno=int(input("Enter your Account Number:"))
Acn=input("Enter Your Account Name:")
Acamount=int(input("Enter Amount:"))
bank1.openAccount(Acno,Acn,Acamount)

while True:
    print("*"*40)
    print("1. Deposit Amount")
    print("2. Withdraw Amount")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*40)
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        amount=int(input("Enter Your Deposit Amount:"))
        bank1.Deposit(amount)
        print("*" * 40)
    elif choice==2:
        amount=int(input("Enter Your Withdrawal Amount:"))
        bank1.Withdraw(amount)
        print("*" * 40)
    elif choice==3:
        bank1.Checkbalance()
        print("*" * 40)

    else:
        print("Thank you for using our service")
        print("*" * 40)
        break

