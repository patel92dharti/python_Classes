def OddEven(a):
    if a%2==0:
        print(a,"is a Even")
    else:
        print(a,"is a Odd")
def Maxoftwo(a,b):
    if a>b:
        print(a,"Is Max")
    else:
        print(b,"Is Max")
def MaxofThree(a,b,c):
    if a>b:
        if a>c:
            print(a,"Is Max")
        else:
            print(c,"Is Max")
    elif b>c:
        print(b,"Is Max")
    else:
        print(c,"Is max")

def fibonacci(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()
def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(n,"Its Non Prime")
                break
        else:
            print(n,"Its Prime")
    else:
        print(n,"Its Non Prime")

def Pattern(n):
    for i in range(1,n):
        print("*"*i)



