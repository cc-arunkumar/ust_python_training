with open("Example.txt",'w') as file:
    file.write("Wt: 81 kg\n")
    file.write("Ht: 170 cm\n")
    file.write("State: Odisha\n")
    
    file.close()
with open("Example.txt",'r') as file:
    content=file.read()
    print(content)
    file.close()
import os
if os.path.exists("Example.txt"):
    with open("Example.txt",'r') as file:
        content=file.read()
        print(content)
        file.close()
else:
    print("The file does not exist")

with open("Example.txt",'r') as file:
    cout=1
    for line in file:
        print("Line",cout,".",line.strip())
        cout+=1
        

