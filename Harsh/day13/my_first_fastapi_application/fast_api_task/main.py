from fastapi import FastAPI, Query
from typing import List
app = FastAPI()

@app.get("/greet")
def greet(name:str="harsh"):
    return {"name" : f"{name}"}

@app.get("/greet")
def greet(name:str):
    return {"name" : f"{name}"}

@app.get("/square/{num}")
def square(num:int):
    return {"Square":f"{num*num}"}

@app.get("/check/{num}")
def even_odd(num:int):
    if num %2==0:
        return{"number":f"{num} is even"}
    else:
        return{"number":f"{num} is odd"}
    
@app.get("/add")
def add(num1:int,num2:int):
    return{"addition of nums":f"{num1+num2}"}

@app.get("/user/{age}")
def user(age:int,city:str):
    return{"user_id":f"{age}",
           "city":f"{city}"
           }

@app.get("/repeat")
def repeat(msg:str,times:int):
    return{"repeating mssg":f"{msg*times}"}

@app.get("/fullname")
def fullname(first: str, last: str):
    return {"fullname": f"{first} {last}"}


@app.get("/upper")
def to_upper(text: str):
    return {"uppercase": f"{text.upper()}"}

@app.get("/area")
def area(length: int, width: int):
    return {"area": length * width}


@app.get("/age/{current_age}")
def age_next_year(current_age: int):
    return {"next_year_age": current_age + 1}


@app.get("/contains")
def contains(word: str, char: str):
    return {"contains": char in word}


@app.get("/movie/{title}")
def movie_info(title: str, year: int, rating: int):
    return {"title": title, "year": year, "rating": rating}


@app.get("/nums")
def nums(n: List[int] = Query(...)):
    return {"numbers": n}

@app.get("/substring")
def substring(text: str, start: int, end: int):
    return {"substring": text[start:end]}

@app.get("/checkpass")
def check_password(pwd: str):
    return {"valid": len(pwd) >= 8}

@app.get("/temp")
def temp(c: float):
    return {"C": c, "F": (c * 9/5) + 32}

@app.get("/task/{task_name}")
def task(task_name: str, priority: str = "normal"):
    return {"task": task_name, "priority": priority}


@app.get("/reverse")
def reverse_text(text: str):
    return {"reversed": text[::-1]}


@app.get("/mul/{a}")
def multiply(a: int, b: int):
    return {"result": a * b}


@app.get("/eligible")
def eligible(age: int):
    return {"eligible": age >= 18}

