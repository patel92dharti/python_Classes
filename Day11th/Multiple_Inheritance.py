class A:
    def getA(self,a):
        self.a=a*2
    def putA(self):
        print("A is",self.a)
class B:
    def getB(self,b):
        self.b=b*2
    def putB(self):
        print("B is",self.b)
class C(A,B):
    def getC(self,c):
        self.c=c*2
    def putC(self):
        print("C is",self.c)

c1=C()
c1.getA(int(input("Enter the A value:")))
c1.getB(int(input("Enter the B value:")))
c1.getC(int(input("Enter the C value:")))

c1.putA()
c1.putB()
c1.putC()