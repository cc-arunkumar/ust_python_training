feedback = {
 "Arjun": 5,
 "Neha": 4,
 "Vikram": 3,
 "Ravi": 4,
 "Fatima": 5
}

# "Priya": 4 .

feedback["Priya"]=4
print(feedback)

for key,val in feedback.items():
    if key=="Ravi" and feedback.get(key)!=5:
        feedback[key]+=1
print(feedback)

length=len(feedback)
sum=0
for key,val in feedback.items():
    sum+=feedback[key]
print(f"Average Value :{sum/length:.2f}")

my_dict={}
for key,val in feedback.items():
    if feedback[key]>=4:
        my_dict[key]="Excellent"
    else:
        my_dict[key]="Needs Improvement"
print(my_dict)

# ===========smaple Execution==========
# {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 4, 'Fatima': 5, 'Priya': 4}
# {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 5, 'Fatima': 5, 'Priya': 4}
# Average Value :4.33
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}