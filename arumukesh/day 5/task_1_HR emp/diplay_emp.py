def dis_emp():
    with open("employees.txt","r")as file:
        content=file.read()
        print(content)

