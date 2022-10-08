T=(1,2,4,[100,200,400,500],10,50,1.5,"Tops",True,False)

print(T)
print(T.index("Tops"))
T[3].append(150)
print(T[3])
T[3].pop(2)
print(T[3])
print(T.count(1))
for i in T:
    print(i)



