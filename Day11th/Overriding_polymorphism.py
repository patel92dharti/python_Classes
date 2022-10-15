class A:
    def Show(self):
        print("Show in Class A")

class B(A):
    def Show(self):
        super().Show()
        print("Show in Class B")

class C(B):
    def Show(self):
        super().Show()
        print("Show in Class C")
c1=C()
c1.Show()

