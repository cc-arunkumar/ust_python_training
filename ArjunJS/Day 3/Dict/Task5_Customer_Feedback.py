#Task 5: Customer Feedback Rating Analyzer
feedback = {
 "Arjun": 5,
 "Neha": 4,
 "Vikram": 3,
 "Ravi": 4,
 "Fatima": 5
}
feedback["Priya"]=4
feedback["Ravi"]+=1 if feedback["Ravi"]!=5 else ""
for i in feedback:
    if(feedback.get(i)==5):
        print(f"Rating 5 : {i}")
print(f"Average rating : {round(sum(feedback.values())/len(feedback),2)}")
new_dict={}
for i in feedback:
    if(feedback.get(i)>=4):
        new_dict[i]="Excellent"
    else:
        new_dict[i]="Need Improvement"
print(f"New dict : {new_dict}")
#Output
# Rating 5 : Arjun
# Rating 5 : Ravi
# Rating 5 : Fatima
# Average rating : 4.33
# New dict : {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Need Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}