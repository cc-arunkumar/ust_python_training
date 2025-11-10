#customer feedback system



feedback = {"Arjun": 5,"Neha": 4,"Vikram": 3,"Ravi": 4,"Fatima": 5}
feedback["Priya"]=4
if feedback["Ravi"]<5:
    feedback["Ravi"]+=1
top_rated=[name for name, rating in feedback.items() if rating == 5]
print("Customers with rating 5:",top_rated)
average_rating=sum(feedback.values())/len(feedback)
print("Average customer rating:", round(average_rating, 2))
performance={
    name:("Excellent" if rating >= 4 else "Needs Improvement")
    for name, rating in feedback.items()
}
print("Customer performance summary:")
for name, status in performance.items():
    print(f"{name}: {status}")

#sample output
# Customers with rating 5: ['Arjun', 'Ravi', 'Fatima']
# Average customer rating: 4.33
# Customer performance summary:
# Arjun: Excellent
# Neha: Excellent
# Vikram: Needs Improvement
# Ravi: Excellent
# Fatima: Excellent
# Priya: Excellent
