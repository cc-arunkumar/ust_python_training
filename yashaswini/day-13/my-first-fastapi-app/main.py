# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def home():
#     return {"message": "Hello FastAPI + UVI"}


# @app.get("/greet/{yashu}")
# def greet(yashu:str):
#     return {"message" : f"Gud Afternoon {yashu}"}


# @app.get("/add")
# def add (num1:int,num2:int,num3:int):
#     return {"sum":num1+num2+num3}


# @app.get("/square/{num}")
# def square(num:int):
#     return {f"square:{num**2}"}


# @app.get("/square")
# def square(num:int):
#     return {f"square:{num**2}"}


from fastapi import FastAPI, Query

app = FastAPI()

# Root endpoint
@app.get("/")
def home():
    return {"message changed"}   

# Greeting endpoint
@app.get("/greet")
def greet(name: str):
    return {"message": f" welcome {name}"}   

# Square endpoint
@app.get("/square/{num}")
def square(num: int):
    return {f"Square of {num} = {num**2}"}   

# Even/Odd check
@app.get("/check/{num}")
def check(num: int):
    if num % 2 == 0:
        return {f"{num} is even"}   
    else:
        return {f"{num} is odd"}    

# Addition
@app.get("/add")
def add(num1: int, num2: int):
    return {"sum=": num1 + num2}    

# User info
@app.get("/user/{id}")
def add(id: int, city: str = "UNKNOWN"):
    return {f"User ID: {id} City: {city}"}   

# Repeat message
@app.get("/repeat")
def repeat(msg: str, times: int):
    for _ in range(times):
        print(msg)   

# Full name
@app.get("/fullname")
def fullname(first: str, last: str):
    return {f"Full Name: {first} {last}"}   

# Uppercase text
@app.get("/upper")
def upper(text: str):
    return {f"Text in Upper Case: {text.upper()}"}   

# Area calculation
@app.get("/area")
def area(length: int, width: int):
    return {f"Area = {length*width}"}   

# Age endpoint
@app.get("/age/{age}")
def age(age: int):
    return {f"Age : {age}"}   

# Contains check
@app.get("/contains")
def age(word: str, char: str):
    if char in word:
        return {f"{char} is present in {word}"}   
    else:
        return {f"{char} is not present in {word}"}   

# Movie info
@app.get("/movie/{name}")
def age(name: str, year: int, rating: int):
    return {f"Movie name: {name} | Year: {year} | Rating: {rating}"}   

# Numbers list
@app.get("/nums")
def age(n: list[int] = Query(...)):
    return {f"List of nummbers: {n}"}   

# Substring
@app.get("/substring")
def age(text: str, start: int, end: int):
    return {f"Substring: {text[start:end]}"}   

# Password check
@app.get("/checkpass")
def age(pwd: str):
    if len(pwd) > 8:
        return {f"Password Success"}  
    else:
        return {f"Password must contain minimun 8 values"}   

# Temperature conversion
@app.get("/temp")
def age(c: int):
    return {f"Temparature in Fahrenheit: {(9/5)(c)+32}"}   

# Task endpoint
@app.get("/task/{clean_room}")
def age(clean_room: int, priority: str):
    return {f"Clean Room no: {clean_room} | Priority: {priority}"}   

# Reverse text
@app.get("/reverse")
def age(text: str):
    return {f"Reversed text of {text} : {text[::-1]}"}   

# Multiplication
@app.get("/mul/{num1}")
def age(num1: int, num2: int):
    return {f"Product of {num1} and {num2} : {num1*num2}"}   

# Eligibility check
@app.get("/eligible")
def age(age: int):
    if age > 18:
        return {"You are Eligible"}   
    else:
        return {"Age below 18"}       
