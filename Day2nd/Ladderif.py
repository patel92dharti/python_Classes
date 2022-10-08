rno = int(input("Enter Roll No:"))
sname = input("Enter Your Name:")
s1 = int(input("Please enter your subject S1 marks:"))
#if s1>=100:
    #print(int(input("Please enter your subject S1 marks again:")))

s2 = int(input("Please enter your subject S2 marks:"))
s3 = int(input("Please enter your subject S3 marks:"))


total= s1+s2+s3
per=total/3
print("Roll No.: ",rno)
print("Full name: ",sname)
print("Total Marks: ",total)
print("Percentage: ",per)
if per>=70:
    print("Distinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass")
else:
    print("Fail")

