#Task 5: Customer Feedback Rating Analyzer
feedback = { "Arjun": 5, "Neha": 4, "Vikram": 3, "Ravi": 4,"Fatima": 5}
feedback[ "Priya"]=4
x=feedback["Ravi"]
if(x!=5):
    feedback["Ravi"]+=1

sum=0;
len=0;
for key,value in feedback.items():
    len+=1
    sum+=value
    if(value==5):
        print(key)
    
dict={}
for key,value in feedback.items():
    if(value>=4):
        dict[key]="Excellent"
    else:
        dict[key]="Needs Improvement"

print(dict)

# #Sample output
# Arjun
# Ravi
# Fatima
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}
