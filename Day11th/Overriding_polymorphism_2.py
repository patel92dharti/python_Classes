class A:
    def Show(self):
        super().Show()
        print("Show in Class A")

class B:
    def Show(self):
        print("Show in Class B")

class C(A,B):
    def Show(self):
        super().Show()
        print("Show in Class C")
c1=C()
c1.Show()

