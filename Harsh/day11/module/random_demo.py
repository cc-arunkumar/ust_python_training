from random import randint,shuffle,choice
print("Random value between 1000 and 9999 is:", randint(1000, 9999))

fruits=["apple","banana","mango","grape","orange"]
print("Random fruit selected is:", fruits[randint(0, len(fruits)-1)])
print(shuffle(fruits))
print(fruits)

print(choice(fruits))
