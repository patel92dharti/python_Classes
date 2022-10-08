Dic={1:"Vishal",2:"Ashish",3:"Dharti",12:[100,200,300],4:"Test",5:"User1",6:"User2"}

print(Dic)
print(Dic.values())
print(Dic.keys())
print(Dic.items())
print(Dic.get(5))
Dic.pop(5)
print(Dic)

Dic1={7:"User5",5:"User4"}
Dic.update(Dic1)
print(Dic)
Dic.popitem()
print(Dic)

for i in Dic:
    print(i,":",Dic[i])

