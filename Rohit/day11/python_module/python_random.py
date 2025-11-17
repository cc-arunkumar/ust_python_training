from random import randint,shuffle,choice

print (randint(2,9))

otp = randint(100000, 999999)
print("Your OTP is:", otp)

fruits = ["banana","apple", "orange","grapes","papaya","watermelon","coconut"]
print("oroginal list", fruits)

print(shuffle(fruits))
print("second list",fruits)
print(" ")
print(choice(fruits))