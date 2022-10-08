# Function with No Argument and No return Value
def printline():
    print("*"*50)

printline()
print("Welcome to User define Function")
printline()


# Function with Argument and No return Value
def addtions(a,b):
    print("Addtions: ",a+b)

printline()
x=int(input("Enter Value: "))
y=int(input("Enter Value: "))
addtions(x,y)
printline()

# Function with Argument and return Value
def substraction(a,b):
    return a-b
printline()
x=int(input("Enter Value: "))
y=int(input("Enter Value: "))
#z=substraction(x,y)
print("Substraction Value: ",substraction(x,y))
printline()