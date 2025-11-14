a1=int(input("Enter a number:" ))
a2=int(input("Enter a number: "))
try:
    print(f"sum={a1+a2}")
    print(f"sub={a1-a2}")
    print(f"mul={a1*a2}")
    print(f"div={a1/a2}")
except ZeroDivisionError:
    print("Zero division error")
except Exception:
    print("expection is raised")