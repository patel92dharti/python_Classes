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

b1=B()
b1.getA(int(input("Enter the A value:")))
b1.getB(int(input("Enter the B value:")))
b1.putA()
b1.putB()
