for i in range(20):
    print("*"* i)

for i in range(20,1,-1):
    print("*"* i)

for i in range(1,20):
    print(" "*(19-i),"*"*i)

for i in range(1,20):
    print(" "*(19-i)," *"*i)
for a in range(1,20):
    print("          "*(19-a),"*"*a)


#rows=10
for num in range(1,10):
    for i in range(num):
        print(num,end=" ")
    print(" ")
