import os


if os.path.exists("file01.txt"):
    with open("file01.txt","a") as file:
        file.write("Append the first line")
        file.write("Append the second line")
else:
    print("Not exist")
print("appended completes")
    