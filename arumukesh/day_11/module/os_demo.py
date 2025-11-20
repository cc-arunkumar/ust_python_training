import os

# print(os.getcwd())
# print(os.listdir())
# current = os.getcwd() + "/akhil_praveen/day11/module"
# if os.path.exists(current+"/dummy_txt.txt"):
#     os.rename(current+"/dummy_txt.txt",current+"/file.txt")
# else:
#     print("already exists")
    
# current+="/akhil_praveen/day11/module"
# # print(os.listdir(current))

target = current = os.getcwd() + "/akhil_praveen/day11/module"
new_file = ""

if not os.path.exists(target+"/final"):
    print("No directory exists")
    os.mkdir(os.path.join(target,"final"))

else:
    print("directory exists")
    with open(target+"/final/final_report.txt","w") as file:
        file.write("hello")
    print("file write complete")
    