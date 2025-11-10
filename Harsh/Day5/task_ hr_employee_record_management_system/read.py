import os
def read():
    if os.path.exists("employees.txt"):
        with open("employees.txt","r") as file:
            content=file.read()
            print(content)
    else:
        print("does not exist")


