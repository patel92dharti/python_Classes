print("Start Code")
data=open("data.txt","w")
try:
    a= int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a/b
    print("Division Value: ",c)
    l=[1,2,3,4,4,8]
    index = int(input("Enter the Index number:"))
    print("Index Value", l[index])
    da=str(list[l])
    data.write(da)

except Exception as e:
    print("Exeption Caught:",e)
finally:

    #data=open("data.txt","r")
    #print(data.read())
    data.close()
    print("End Code")

