import random

Pass1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','s','t','u','v','w','x','y','z','1','2',
       '3','4','5','6','7','8','9','0','!','@','#','$','%','&','*','?','~']

password=" "

for i in range(16):
    password=password+ random.choices(Pass1)[0]

print("Your New Password is:\n",password)
