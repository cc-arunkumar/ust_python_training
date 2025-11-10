# Task 5: Customer Feedback Rating
# Analyzer
# Scenario:
# Your customer service team collects feedback in a dictionary form
# where key = customer name, value = their rating (out of 5).


feedback={
"Arjun":5,
"Neha":4,
"Vikram":3,
"Ravi":4,
"Fatima":5
}

feedback["Priya"]=4

if feedback["Ravi"]<5:
    feedback["Ravi"]+=1

five_star=[n for n,r in feedback.items() if r==5]
print("Customers with Rating 5:",five_star)

avg=sum(feedback.values())/len(feedback)
print("Average Rating:",round(avg,2))

result={n:("Excellent" if r>=4 else "Needs Improvement") for n,r in feedback.items()}
print(result)

# sample output

# Customers with Rating 5: ['Arjun', 'Ravi', 'Fatima']
# Average Rating: 4.33
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}