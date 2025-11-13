# Part 3: Function with arguments and without return
def employee(ename,dname,efficiency):
    print("Name:",ename)
    print("dname:",dname)
    if(efficiency>25):
        print("excellent")
    elif(efficiency >15 and efficiency<25):
        print("good performanse")


employee("sai","cse",45)



#Name: sai
# dname: cse
# excellent