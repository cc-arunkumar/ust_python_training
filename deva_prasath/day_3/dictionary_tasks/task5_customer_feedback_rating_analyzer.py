# customer_feedback_rating_analyzer.py
# Your customer service team collects feedback in a dictionary form
# where key = customer name, value = their rating (out of 5)

feedback = {
 "Arjun": 5,
 "Neha": 4,
 "Vikram": 3,
 "Ravi": 4,
 "Fatima": 5
}
feedback['Priya']=4
print("After Priya addition: ",feedback)


for key,val in feedback.items():
    if key=="Ravi" and val!=5:
        feedback[key]=5

for key,val in feedback.items():
    if val==5:
        print("Customers with  rating of 5: ",key)
        
sumi=0
for val in feedback.values():
    sumi+=val
avg=sumi//len(feedback)
print("Average rating: ",avg)
print(avg)
new_dict={}
for key,val in feedback.items():
    if val>=4:
        new_dict[key]="Excellent" 
    else:
        new_dict[key]="Needs Improvement"
print("Final dict:",new_dict)

#Sample output

# After Priya addition:  {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 4, 'Fatima': 5, 'Priya': 4}
# Customers with  rating of 5:  Arjun
# Customers with  rating of 5:  Ravi
# Customers with  rating of 5:  Fatima
# Average rating:  4
# 4
# Final dict: {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}