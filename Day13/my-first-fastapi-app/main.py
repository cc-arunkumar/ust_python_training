from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/")
def home():
    return {"message changed"}

@app.get("/greet")
def greet(name:str):
    return {"message":f" welcome {name}"}


# @app.get("/square")
# def square(num:int = 1):
#     return {f"Square of {num} = {num**2}"}

@app.get("/square/{num}")
def square(num:int):
    return {f"Square of {num} = {num**2}"}

@app.get("/check/{num}")
def check(num:int):
    if num%2==0:
        return {f"{num} is even"}
    else:
        return {f"{num} is odd"}
    
@app.get("/add")
def add(num1:int,num2:int):
    return {"sum=":num1+num2}

@app.get("/user/{id}")
def add(id:int,city:str="UNKNOWN"):
    return {f"User ID: {id} City: {city}"}
    
@app.get("/repeat")
def repeat(msg:str,times:int):
    for _ in range(times):
        print(msg)
        
@app.get("/fullname")
def fullname(first:str,last:str):
    return {f"Full Name: {first} {last}"}

@app.get("/upper")
def upper(text:str):
    return {f"Text in Upper Case: {text.upper()}"}

@app.get("/area")
def area(length:int,width:int):
    return {f"Area = {length*width}"}

@app.get("/age/{age}")
def age(age:int):
    return {f"Age : {age}"}

@app.get("/contains")
def age(word:str,char:str):
    if char in word:
        return {f"{char} is present in {word}"}
    else:
        return {f"{char} is not present in {word}"}
    
@app.get("/movie/{name}")
def age(name:str,year:int,rating:int):
    return {f"Movie name: {name} | Year: {year} | Rating: {rating}"}

@app.get("/nums")
def age(n:list[int]=Query(...)):
    return {f"List of nummbers: {n}"}

@app.get("/substring")
def age(text:str,start:int,end:int):
    return {f"Substring: {text[start:end]}"}

@app.get("/checkpass")
def age(pwd:str):
    if len(pwd) >8:
        return {f"Password Success"}
    else:
        return {f"Password must contain minimun 8 values"}
    
@app.get("/temp")
def age(c:int):
    return {f"Temparature in Fahrenheit: {(9/5)(c)+32}"}

@app.get("/task/{clean_room}")
def age(clean_room:int,priority:str):
    return {f"Clean Room no: {clean_room} | Priority: {priority}"}

@app.get("/reverse")
def age(text:str):
    return {f"Reversed text of {text} : {text[::-1]}"}

@app.get("/mul/{num1}")
def age(num1:int,num2:int):
    return {f"Product of {num1} and {num2} : {num1*num2}"}

@app.get("/eligible")
def age(age:int):
    if age>18:
        return {"You are Eligible"}
    else:
        return {"Age below 18"}