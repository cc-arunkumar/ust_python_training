#sales record analyzer


tuple1=(("chennai",85000),("banglore",92000),("hyderabad",78000),("pune",102000),("delhi",98000))
for branch_name,total_sales in tuple1:
    if total_sales>90000:
        print("branches with sales above 92000",branch_name)
values=[total for _,total in tuple1]
average_sales=sum(values)/len(values)
print("average sales",average_sales)

lowest_sales=tuple1[0]
for branch_name in tuple1:
    if branch_name[1]<lowest_sales[1]:
        lowest_sales=branch_name
print("branch with lowest sales",lowest_sales)

tuple2=list(tuple1)
for i in range(len(tuple2)):
    if tuple2[i][0].lower()=="pune":
        tuple2[i]=("pune",105000)
updated_tuple=tuple(tuple2)
for branch_name,total_sales in updated_tuple:
    print("branch name",branch_name,"Total sales",total_sales)
    
# sample output
# branches with sales above 92000 banglore
# branches with sales above 92000 pune
# branches with sales above 92000 delhi
# average sales 91000.0
# branch with lowest sales ('hyderabad', 78000)
# branch name chennai Total sales 85000
# branch name banglore Total sales 92000
# branch name hyderabad Total sales 78000
# branch name pune Total sales 105000
# branch name delhi Total sales 98000