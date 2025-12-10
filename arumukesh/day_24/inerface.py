from employees_crud import create_one,insert_many,read_by_column,read_by_proj_stat,read_by_length,update_dept,increment_exp,remove_address
# print("""Enter Operation to be executed 
#       1.Insert
#       2.Read
#       3.Update
#       4.Delete""")

# action=int(input("Enter Choice: "))

# if action==1:
#     print("""select the choice of insert:
#           1.insert one
#           2.Bulk insert
#           """)
#     sub_action=int(input("ENter insert function "))
#     if sub_action==1:
#         create_one()
#     if sub_action==2:
#         insert_many()
# # create_one()
# insert_many()
# if action==2:
#     print("""Enter Type of read action:
#           1.Read By Column
#           2.Read by project status 
#           3.read employees working on more than 1 project""")
#     sub_action=int(input("Enter read action :"))
#     if sub_action==1:
#         column=input("enter the column")
#         value=input("enter the value for the column")
#         read_by_column(column,value)
#     if sub_action==2:
#         status=input("enter the required status of the project")
#     # read_by_column("name","Karen")
#         read_by_proj_stat(status)
#     if sub_action==3:
#         read_by_length()
        
# if action==3:
    
#     sub_action=int(input("Enter read action :"))
    
# read_by_length()
# update_dept("6937e527096cface255cd090","IT")

# increment_exp("6937e527096cface255cd090")

remove_address()
