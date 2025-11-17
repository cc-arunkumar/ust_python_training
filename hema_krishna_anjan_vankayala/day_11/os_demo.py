import os 
# print("Current DIrectory:", os.getcwd())
# print("List of files and directories:", os.listdir())

# new_dir = 'sub_dir'
# if not os.path.exists(new_dir):
#     os.mkdir(new_dir)
# else:
#     print("File Name already exists....")
#create a file

# if not os.path.exists('dummy_file.txt'):
#     with open('dummy_file.txt','w') as file: 
#         pass 
# else:
#     os.rename('dummy_file.txt','final_file.txt')

target_path = os.getcwd() + '/final_dir'
new_file = 'final_report.txt'
if not os.path.exists(target_path):
     os.mkdir('final_dir')
else:
    print("Dir Already Exists....")

new_file_path = os.path.join(target_path,new_file)
with open(new_file_path,'w') as file: 
    pass

# print("List of files and directories:", os.listdir())