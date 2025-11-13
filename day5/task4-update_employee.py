upd_id = "E104"
upd_sal = 40000
 
lines = []
flag = False
 
with open("employeedata.txt", "r") as file:
    for line in file:
        var = line.strip().split(",")
        if var[0].lower() == upd_id.lower():
            var[3] = str(upd_sal)
            flag = True
        lines.append(",".join(var))
 
if flag:
    with open("employeedata.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")
    print(f"\nUpdated Record:\n{','.join(var)}")
else:
    print("Employee not found")
    
    # output
# Updated Record:
# E106,Meera Nair,HR,64000,2022-11-20