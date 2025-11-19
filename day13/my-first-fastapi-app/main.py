from fastapi import FastAPI

app=FastAPI()

@app.get("/")

def home():
    return {"message":"fast api demo"}

# query parameter
@app.get("/greet/{name}")
def greet(name:str):
    return{"message": f" good morning, {name}"}

#addition
@app.get("/add")
def add(num1:int,num2:int,num3:int):
    return {"sum=":num1+num2+num3}


# square
@app.get("/square")
@app.get("/square/{num}")
def square(num:int=9):
    return{"square=": num**2}

#even or odd
@app.get("/evenodd/{num}")
def evenodd(num:int):
    if num%2==0:
        return {"message":f"{num} is even"}
    else:
        return {"message":f"{num} is odd"}

# age 
@app.get("/users/{num}")
@app.get("/users")
def userinfo(age:int=24,city:str="atp"):
    return{"message":f"users age is {age} and city={city}"}

# repeat a message n times
@app.get("/repeat")
def repeat(msg:str,times:int):
    return{"repeat: ":msg*times}
    
# full name
@app.get("/fullname")
def fullname(first:str,last:str):
    return{"fullname: ": first+last}

# string to upper case
@app.get("/uppercase")
def upper(word:str):
    return{"upper case word:":word.upper()}

# area of triangle
@app.get("/area_of_triangle")
def area_of_triangle(length:int,breadth:int):
    return{"area of triangle:":length*breadth}

#age next year
@app.get("/age_next_year{age}")
def age_next_year(age:int=24):
    return{"age next year is:":age+1}

# character present in word
@app.get("/char_contains_in_word")
def char_contains_in_word(word:str,char:str):
    if char in word:
        return{f"{char} is in word"}
    else:
        return{f"{char} is not in word"}
    
# Combine path + multiple query params
@app.get("/movie/{name}")
def movie(name:str,year:int=2009,rating:int=9):
    return{"message":f"{name} {year} {rating}"}

# return list os numbers
from fastapi import Query
@app.get("/nums")
def get_nums(num1:list[int]=Query(...)):
    return {"message":f"numbers:{num1}"}

# show substring of string
@app.get("/substring_of_a_string")
def substring(name:str,start:int,end:int):
    return{"message":f"{name[start:end]}"}

# validate 
@app.get("/validate")
def validate(password:str):
    if password.isalnum() and len(password)==10:
        return {"message":f"{password} is valid"}
    else:
        return {"message":f"{password} is invalid"}
    
# Temperature
@app.get("/temperature/{celcius}")
def temperature(celcius:int):
    return {"message":f"celsius {celcius}"}
        
#task with priority
@app.get("/task/{room}")

def check(room:str,priority:str="high"):
    return {"message": f" {room } with {priority} priority"}

#reverse text
@app.get("/reverse")
def reverse(text:str):
    return {"message":f"{text[::-1]}"}

#mutliply 2 numbers
@app.get("/mul/{num}")
def multiply(n1:int,n2:int=9):
    return {"message":f"product:{n1*n2}"}

# age eligibility
@app.get("/eligible")
def eligibility(age:int):
    if age>=18:
        return {"message":f"{age} is eligible"}
    else:
        return {"message":f"{age} is not eleigible"}