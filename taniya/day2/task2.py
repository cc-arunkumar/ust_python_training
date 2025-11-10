salary = int(input("enter salary "))
bonus_cal = (lambda salary:salary +(salary*0.10))

print(bonus_cal(salary))