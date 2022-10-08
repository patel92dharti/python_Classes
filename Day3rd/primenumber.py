#3,5, 7, 11,13,17,19,23,37,41,43,47,53...

n = int(input("Enter The N value:"))
#if n%2!=0:
if n%2>0:
    for i in range(3,int(n/2)+1,2):
        if n%i == 0:
            print(n,"is not Prime Number")
            break
    else:
        print(n,"is Prime Number")
else:
    print("Try again")