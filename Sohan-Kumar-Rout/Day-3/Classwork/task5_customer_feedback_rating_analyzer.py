#Task 5: : Customer Feedback Rating Analyzer

#Code 
feedback = {
 "Arjun": 5,
 "Neha": 4,
 "Vikram": 3,
 "Ravi": 4,
 "Fatima": 5
}
feedback["Priya"]=4
feedback["Ravi"]+=1 if feedback["Ravi"]<5 else 0
for customers,rating in feedback.items():
    if(rating==5):
        print("Rating Equals to 5 : ",customers)

average_rating = sum(feedback.values()) / len(feedback)

result = {n: ("Excellent" if r >= 4 else "Needs Improvement") for n, r in feedback.items()}

print(result)

#Output 
# Rating Equals to 5 :  Arjun
# Rating Equals to 5 :  Ravi
# Rating Equals to 5 :  Fatima
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}

