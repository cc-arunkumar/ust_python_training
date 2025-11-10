# file = open("t1.txt", "r")

# content = file.read()
# print(content)

with open("t1.txt", "r") as file:
    i = 1
    word = "concepts"
    for line in file:
            print("word found !")
            print("Line ", i, line.strip())
            i += 1
        
