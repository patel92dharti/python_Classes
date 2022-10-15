#In Python, Overloding concept not supportable,..........
class Tops:
    def test(self):
        print("No Argument pass")
    def test(self,a):
        print("1 Argument Pass")
    def test(self,a,b):
        print("2 Argument Pass")

t1=Tops()
#t1.test()
#t1.test(10)
t1.test(10,23)
