l=[1,3,4.4,"Dharti","Tops","Apple",4,56,10,"Py0",True,300,500,False]

print(l)
print(type(l))
#append add eliments in last
l.append(100)
print(l)

#Count of Aliments
print(l.count(1))
print(l.index(False))
#ll= l.copy():- Copy New Structure
ll= l.copy()
print(ll)
ll.pop()
print(ll)
print(l)
#dha=l :- only point to new variable not crate struct
dha=l
print(dha)
dha=[11,22,33,444,55]
l.extend(dha)
#dha.insert(10,1522)
print(l)
l.remove(False)
print(l)
l.reverse()
print(l)
"""pop function 2 types remove list:- 
    1.Only pop() remove last aliments
    2. pop(2) remove aliments index wise
"""
l.pop(1)
print(l)
l.clear()
print(l)
print(ll)
print(dha)