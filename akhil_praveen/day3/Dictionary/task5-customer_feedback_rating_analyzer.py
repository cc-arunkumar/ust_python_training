# Customer_Feedback_Rating_Analyzer

feedback = {
 "Arjun": 5,
 "Neha": 4,
 "Vikram": 3,
 "Ravi": 4,
 "Fatima": 5
}

feedback["Priya"]=4

if feedback["Ravi"]==4:
    feedback["Ravi"]+=1

avg=0
print("All customers with rating 5: ")
for i in feedback:
    avg+=feedback[i]
    if feedback[i]==5:
        print(i)

print("Average ratings: ",avg/len(feedback))

new_feedback={key:("Excellent" if value>4 else "Needs improvement") for key,value in feedback.items()}
for i in new_feedback:
    print(f"{i} -> {new_feedback[i]}")

# All customers with rating 5: 
# Arjun
# Ravi
# Fatima
# Average ratings:  4.333333333333333
# Arjun -> Excellent
# Neha -> Needs improvement
# Vikram -> Needs improvement
# Ravi -> Excellent
# Fatima -> Excellent
# Priya -> Needs improvement