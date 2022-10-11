print("Start Code")

try:
    a= int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a/b
    print("Division Value: ",c)
    l=[1,2,3,4,4,8]
    index=int(input("Enter the Index number:"))
    print("Index Value",l[index])
except Exception as e:
    print("Exeption Caught:",e)
finally:
    print("End Code")
