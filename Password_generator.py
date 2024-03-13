import random

characters =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_signs = "+-/*!&$#?=@"
numbers = "1234567890"
password = ""
i = 0
j = int(input("How many characters your password should have: "))
if j < 8:
    print("Password must contain at least 8 characters!")
elif j > 50:
    print("The password can only have a maximum of 50 characters!")
else:
    rand_sign = random.randint(0,25)
    sign = uppercase[rand_sign]
    password = password + sign
    rand_sign = random.randint(0,10)
    sign = special_signs[rand_sign]
    password = password + sign
    rand_sign = random.randint(0,9)
    sign = numbers[rand_sign]
    password = password + sign
    while i != j - 3:
        rand_sign = random.randint(0,71)
        sign = characters[rand_sign]
        password = password + sign
        i += 1
    print("Your password: " + password)
