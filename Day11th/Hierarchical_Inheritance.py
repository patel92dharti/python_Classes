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

c1=C()
c1.getA(50)
c1.getC(60)
c1.putC()
c1.putA()

b1=B()
b1.getB(40)
b1.putB()
