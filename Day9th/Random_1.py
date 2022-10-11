import random

num=random.randint(1,20)

while True:
    guess=int(input("Guess a number between 1 to 20: "))
    if guess==num:
        print("you Guessed a number is correct ")
        break
    elif guess>num:
        print("You Guessed a number is Greater ")
    elif guess<num:
        print("you Guessed a number is Smaller ")


