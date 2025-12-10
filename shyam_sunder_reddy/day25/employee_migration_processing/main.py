from mysql_crud import load_data,read_all
from mongo_crud import insert_many_emp,insert_one_emp,update_one_emp,read_all,delete_many_employee,delete_one_employee
from utils import add_new_field


#loading the data from json and uploading to the mysql databse
# load_data()

#reading all the data from the mysql database in dictionary format
# data=read_all()
# print("--------------All the Employees in mysql database----------------")
# for emp in data:
#     print(emp)
   
#function to add extra field    
# data=add_new_field(data)

#function to insert many
# insert_many_emp(data)

#insert one
# emp={
#  "emp_id": 206,
#  "name": "Sham",
#  "department": "AI",
#  "age": 26,
#  "city": "Bangalore",
#  "category":"Fresher"
#  }
# insert_one_emp(emp)

# update 
# update_one_emp(206,"name","shyam")

# #delete one
# delete_one_employee(206)

# #delete many
# delete_many_employee("Cloud")


data=read_all()
for emp in data:
    print(emp)