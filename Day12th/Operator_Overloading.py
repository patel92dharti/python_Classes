class Point:
    def __init__(self,x,y):
        print("Init Called")
        self.x=x
        self.y=y
    def __str__(self):
        print("STR Called")
        return "[{0},{1}]".format(self.x,self.y)
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        print("Add Called")
        return Point(x,y)
p1=Point(10,60)
print("STR call",p1)
p2=Point(20,50)
print("Str 2 call",p2)
print("Addition of Objects",p1+p2)
