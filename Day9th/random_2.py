import random

l=[]
Lucky=[]
for i in range(1,101):
    l.append(i)

for h in range(10):
    num=random.choice(l)
    Lucky.append(num)
    l.remove(num)

print("List of Number: ",l)
print("Your Lucky Number: ",Lucky)

