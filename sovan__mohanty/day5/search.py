with open("Example.txt",'r') as file:
    target="wt: 81 kg\n"
    for line in file:
        if(target==line):
            print("line found")
    file.close()