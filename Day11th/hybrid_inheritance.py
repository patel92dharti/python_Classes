class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A is",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B is",self.b)

class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C is",self.c)
class D(B,C):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D is",self.d)
d1=D()
d1.getD(40)
d1.putD()
d1.getA(10)
d1.putA()
d1.getB(51)
d1.putB()
d1.getC(90)
d1.putC()