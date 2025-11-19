# def main():
#     print("Hello from my-first-fastapi-app!")


# if __name__ == "__main__":
#     main()

from typing import Optional
from fastapi import FastAPI,Query
app = FastAPI()



# @app.get("/")
def hello():
    return {"message":"Hello World welcome to ust"}

# Greet user with optional name (query paramdefault)
@app.get("/great/{name}")
def great(name:str):
    return {"message":f"good afternoon {name} "}


# 4.Simple addition using query params
@app.get("/add")
def add(num1:int,num2:int,num3:int):
    return{"sum=":num1+num2+num3}


# Get square of a number (path param)
@app.get("/square")
def square(num:int=5):
    return{"square":num**2}

# Check if number is even or odd (path)
@app.get("/even_odd/{num}")
def even_odd(num:int):
    if num%2==0:
        return{f"the {num} number is even"}
    else:
        return{f"the {num} number is odd"}
["the 12 number is even"]


# .User info with optional city (path + optional query)

@app.get("/user_info/{num}")
def user_info(num:int,city:str="mumbai"):
    return {f"{num} city:{city}"}


@app.get("/repeat")
def repeat(msg:str,times:int):
    r=msg*times
    return {"number of times msg repeat":r}


@app.get("/name")
def name(first_name:str,scond:str):
    return{f"full name is": f"{first_name}{scond}"}

@app.get("/upper")
def upper(word:str):
    name=word.upper()
    return {"in upper case":{name}}

@app.get("/rectangle")
def rectangle(l:int,b:int):
    return{"area of rectangle":f"{l*b}"}

@app.get("/next_age/{age}")
def next_age(age:int):
    return{"the lest year age":f"{age+1}"}

@app.get("/contains")
def contains(word:str,char:str):
    for i in word:
        if i == char:
            return{"char is in word ":f"{word}"}
        else:
            return{"char is not in word ":f"{word}"}

@app.get("/movie/{word}")
def movie(word:str,year:int,rating:int):
    return{word,year,rating}

@app.get("/nums")
def list_num(n:list[int]=Query()):
    return{f"the list of numbers {n}"}

@app.get("/substring")
def sub_string(text:str,start:int,end:int):
    new=text[start:end]
    return{f"the substring {new}"}

@app.get("/checkpass")
def password(pwd:str):
    if len(pwd)==7:
        return{f"{pwd} it is valid"}
    else:
        return{f"{pwd} is not valid"}
    
@app.get("/temp")
def temp(c:Optional[int],f:Optional[int]):
    if c is not None:
        f=(c*9/5)+32
    elif f is not None:
        c=(f-32)*5/9
    return {"temp in c":c,"temp in f":f}
    
@app.get("/task/clean-room")
def room_priority(priority: str):
    if priority == "high":
        return {"priority is high"}
    elif priority == "medium":
        return {"priority is medium"}
    else:
        return {"priority is low"}
# Reverse text
@app.get("/reverse")
def word_reverse(text: str):
    rev = text[::-1]
    return {f"Word reversing: {rev}"}
# Multiply 2 numbers (path + query)
@app.get("/mul/{num}")
def multiply(num: int, b: int):
    multi = num * b
    return {f"multiply: {multi}"}
# Check age eligibility
@app.get("/eligible")
def age_eligibility(age: int):
    if age >= 18:
        return {"Age if eligible"}
    else:
        return {"Age if Not eligible"}
