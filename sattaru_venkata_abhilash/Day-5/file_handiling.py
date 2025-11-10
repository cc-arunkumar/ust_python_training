# file = open('handle1.txt','r')
# with open("handle1.txt","w") as file:
#     file.write("Hello!World!\n")
#     file.write("Hola! Anjan Kushal")
#     file.close()

# content = file.read()
# print(content)
# file.close()


# with open("handle1.txt","r") as file:
#     content = file.read()
#     print(content)

import os 
# if os.path.exists('handle1.txt'):
#     print("Exist")
# else:
#     print("Not Exist")

# os.remove("handle1")
# i=1
# with open("handle1.txt") as file:
#     for line in file:
#         print("Line ",i,":",line.strip())
#         i += 1

with open("handle1.txt","a") as file:
    file.write("\npgEhvBHi Anjan!")
#PgEhvB