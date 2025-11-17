import random  # Import the random module to generate random numbers and perform random actions

# Generate a random 6-digit OTP (One Time Password) between 100000 and 999999
otp = random.randint(100000, 999999)  
print("OTP: ", otp)  

# List of fruits
fruits = ["Apple", "Grapes", "Mango", "Banana", "Guava", "DragonFruit"]
print("Original fruits: ", fruits)  # Print the original list of fruits

# Shuffle the list of fruits randomly (rearrange elements in a random order)
random.shuffle(fruits)
print(fruits) 

# Select a random fruit from the shuffled list using random.choice()
fruit = random.choice(fruits)
print(fruit)  

#Sample Execution
# OTP:  662586
# Original fruits:  ['Apple', 'Grapes', 'Mango', 'Banana', 'Guava', 'DragonFruit']
# ['Banana', 'Grapes', 'Mango', 'Guava', 'DragonFruit', 'Apple']
# Grapes
