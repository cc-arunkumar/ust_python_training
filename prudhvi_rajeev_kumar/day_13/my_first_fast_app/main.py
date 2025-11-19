from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

@app.get("/greet/{name}")
def greet(name : str):
    return {"message" : f"Hi {name}"}

@app.get("/square/{num}")
def square(a:int):
    return {"message" : f"The square is {a*a}"}

@app.get("/is_even_or_odd/{num}")
def is_even_or_odd(a:int):
    if a % 2 == 0:
        return {"message" : "even"}
    else:
        return{"message" : "odd"}
    
@app.get("/calc_sum/{a}")
def calc_sum(a:int, b:int):
    return {"message" : f"Sum is {a+b}"}

@app.get("/user/{user_id}")
def user_info(user_id: int, city: str = None):
    if city:
        return {"user_id": user_id, "city": city}
    return {"user_id": user_id}

@app.get("/repeat/{msg}")
def repeat(msg : str, num : int):
    result = []
    for i in range(0, num):
        result.append(msg)
    return{"message" : result}

@app.get("/two_names/{first}")
def two_names(first : str, last : str):
    return {"message" : first+last}
        
@app.get("/to_upper")
def to_upper(string: str):
    return {"message" : string.upper()}

@app.get("/calc_area")
def calc_area(length : int, breadth : int):
    return {"message" : f"Area is {length * breadth}"}

@app.get("/age_next_year")
def age_next_year(age : int):
    return {"message" : f"Age next year is {age + 1}"}

@app.get("/word_contains")
def word_contains(word: str, character: str):
    if character in word:
        return {"result": True}
    else:
        return {"result": False}
    
@app.get("get_movie/{movie_name}")
def get_movie(movie_name: str, year: int, rating: int):
    return {
        "movie": movie_name,
        "year": year,
        "rating": rating
    }

@app.get("/nums")
def get_nums(n: List[int] = Query(...)):
    return {"numbers": n}


@app.get("/show_substring")
def show_substring(string: str, start : int, end:int):
    result = ""
    for i in range(start, end+1):
        result += string[i]
    return {"message" : result}

@app.get("/checkpass")
def checkpass(pwd : str, length : int):
    result = len(pwd)
    if result == length:
        return {"message" : True}
    else:
        return {"message" : False}

@app.get("/tempretaure")
def tempretaure(temp : float):
    f = (temp * 9/5) + 32
    return {
        "Celsius": temp,
        "Fahrenheit": f
    }  

@app.get("/get_task/{task_name}")
def get_task(task_name : str, priority: str):
    return {
        "Task" : task_name,
        "Priority" : priority
    }
        

@app.get("/reverse")
def reverse(text : str):
    reversed = text[::-1]
    return{"Reversed Text" : reversed}

@app.get("/multiply/{a}")
def multiply(a:int, b:int):
    return {"Multiplication" : a*b}

@app.get("/check_age_eligiblity")
def check_age_eligiblity(age : int):
    if age <= 18:
        return {"Age Requirements" : "Not Met"}
    if age > 18:
        return {"Age Requirements" : "Met"}

