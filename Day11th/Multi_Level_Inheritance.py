class A:
    def getA(self,a):
        self.a=a*2
    def putA(self):
        print("A is",self.a)
class B(A):
    def getB(self,b):
        self.b=b*2
    def putB(self):
        print("B is",self.b)
class C(B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C is",self.c)

b1=C()
b1.getA(int(input("Enter the A value:")))
b1.getB(int(input("Enter the B value:")))
b1.getC(int(input("Enter the B value:")))

b1.putA()
b1.putB()
b1.putC()