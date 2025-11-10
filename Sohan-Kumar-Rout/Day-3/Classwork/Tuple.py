
#Task 1
task1=(2,3,4,3,5)
# list=[]

# for task in task1:
#     list.append(task * 3)
# print(tuple(list))

#Check Tuple
# for i in range(1,5):
#     if(task1[i]==3):
        
#         print("true")
#         break
        # print(task1[i])

#Unpacking
employees = (
    ("Sohan","Trivandrum","UST"),
    ("Sovan","Kochi","UST")
)
for name,city,company in employees:
    print(name)
    print(city)
    print(company)
    print("---")

