import random
data=open("data.txt","w")
for i in range(20):
    num=random.randint(1,100)
    data.write(str(num)+",")
data.close()


data=open("data.txt","r")
odd=open("odd.txt","w")
even=open("Even.txt","w")
prime=open("prime.txt","w")

l=data.read().split(",")[:-1]


for h in l:
    if int(h)%2==0:
        even.write(h+ ",")
    else:
        odd.write(h+",")
data.close()
odd.close()
even.close()

for d in l:
    if int(d)%2!=0:
        for ll in range(3,int((int(d))/2)+1,2):
            if int(d)%ll==0:
                break
        else:
            prime.write(d+",")


data.close()
odd.close()
even.close()
prime.close()


print("Data File Content:")
data=open("data.txt","r")
print(data.read())
data.close()

print("Odd File Content:")
odd=open("odd.txt","r")
print(odd.read())
odd.close()

print("Even File Content:")
even=open("Even.txt","r")
print(even.read())
even.close()

print("Prime File Content:")
prime=open("prime.txt","r")
print(prime.read())
prime.close()




