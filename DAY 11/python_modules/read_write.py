import os

target_path="DAY 11\\python_modules\\s_demo.txt"

if os.path.exists(target_path):
    print("Path Exist")
else :
    with open(target_path, "w") as new_file:
        new_file.write("New file created")
        new_file.close()

    print(f"File created: {target_path}")