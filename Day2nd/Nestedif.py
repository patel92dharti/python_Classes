a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))
d = int(input("Enter D:"))
if a>b:
    if a>c:
        if a>d:
            print("A is greater")
        else:
            print("D is greater")
    else:
        print("C is greater")
elif c>d:
    print("C is Greater")
else:
    print("D is Greater")

