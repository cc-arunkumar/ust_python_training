import os

if os.path.exists("t1.txt"):
    with open("t1.txt", "r") as file:
        console = file.read()
        print(console)
else:
    print("File not Exists!")

