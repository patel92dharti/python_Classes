se={10,20,30,40,30}
print(se)

for i in se:
    print(i)

se.remove(20)
print(se)
se.add(50)
print(se)
se.discard(10)
print(se)
se.clear()
print(se)
la=[20,30,60,80]
se.update(la)
print(se)