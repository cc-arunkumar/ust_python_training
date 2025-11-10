# IDs=list(map(int,input("Enter all id ").split()))
# even_id = list(filter(lambda x: x%2==0,IDs))
# print(even_id)




# bonus = list(filter(lambda sal: sal>50000,salaries))
# print("salaries",bonus)


user = input("Enter IDs separated by commas: ")


ids = list(map(int, user.split(',')))
even_ids = list(filter(lambda x: x % 2 == 0, ids))

print("Even IDs:", even_ids)
