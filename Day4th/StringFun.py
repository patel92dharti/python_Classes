s=input("Enter String: ")
space=0
character=0
number=0
Alfa=0
alfanumberi=Alfa+number
for i in s:
    character=character+1
    if i.isspace():
        space=space+1

    elif i.isnumeric():
        number=number+1
    elif i.isalpha():
        Alfa=Alfa+1

word_list= str.split(s)
number_of_word=len(word_list)
print("Number of Space:",space)
print("Number of Character:",character)
print("Number of Numerical:",number)
print("Number of Word:",number_of_word)
print("Number of Alfabates:",Alfa)
