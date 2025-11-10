# #Task 5: Customer Feedback Rating Analyzer
# Scenario:
# Your customer service team collects feedback in a dictionary form
# where key = customer name, value = their rating (out of 5).
# Instructions:
# 1. Create the following dictionary:
# feedback = {
#  "Arjun": 5,
#  "Neha": 4,
#  "Vikram": 3,
#  "Ravi": 4,
#  "Fatima": 5
# }
# Dictionary Tasks 4
# 2. Add a new feedback: "Priya": 4 .
# 3. Increase Ravi’s rating by 1 (if not already 5).
# 4. Print all customers with a rating of 5.
# 5. Find the average rating of all customers.
# 6. Create a new dictionary using dictionary comprehension to store:
# key = customer name
# value = "Excellent" if rating ≥ 4, else "Needs Improvement" .
# 7. Print the new dictionary.

feedback = { "Arjun": 5, "Neha": 4, "Vikram": 3, "Ravi": 4,"Fatima": 5}
feedback[ "Priya"]=4
x=feedback["Ravi"]
if(x!=5):
    feedback["Ravi"]+=1

sum=0
len=0
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
