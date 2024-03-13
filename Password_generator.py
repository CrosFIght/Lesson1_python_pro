import random

characters =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
i = 0
j = int(input("How many characters your password should have: "))
while i != j:
    rand_sign = random.randint(0,71)
    sign = characters[rand_sign]
    password = password + sign
    i += 1
print(password)
