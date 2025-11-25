from random import randint, shuffle, choice   # Import specific random functions

# Generate a random integer between 2 and 9 (inclusive)
print(randint(2, 9))

# Generate a random 6-digit OTP
otp = randint(100000, 999999)
print("Your OTP is:", otp)

# Define a list of fruits
fruits = ["banana", "apple", "orange", "grapes", "papaya", "watermelon", "coconut"]
print("original list", fruits)

# Shuffle the list in place (returns None, modifies the list directly)
print(shuffle(fruits))   # This will print 'None' because shuffle works in place
print("second list", fruits)   # The list is now shuffled

print(" ")

# Pick a random fruit from the list
print(choice(fruits))
