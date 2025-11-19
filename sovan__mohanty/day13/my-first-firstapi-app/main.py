# 
from fastapi import FastAPI

app=FastAPI()

# @app.get("/")
# def home():
#     return {"message":"Hello World"}

# # @app.get("/greet/{name}")
# # def greet(name:str):
# #     return {"message":f"GoodBye {name}"}

# @app.get("/add")
# def add(num1 : int,num2 : int,num3 : int):
#     return {"Sum= ":num1+num2+num3}

# @app.get("/square/{num}")
# def square(num: int):
#     return {f"square of {num} is":num*num}

@app.get("/square")
def square(num: int=2):
     return {f"square of {num} is":num*num}

@app.get("/greet")
def greet(name:str):
    return {"name: ":f"{name}"}

# @app.get("/square/{num}")
# def square(num:int):
#     return {f"Square of {num} is: ":num*num}

@app.get("/check/{num}")
def checkevenorodd(num:int):
    if(num%2==0):
        return {f"{num} is even"}
    else:
        return {f"{num} is odd"}
@app.get("/add")
def add(num1 : int,num2 : int):
    return {"Sum= ":num1+num2}

@app.get("/user/24")
def user_info(name:str="Sovan",age:int=24,city: str="Bhubaneswar"):
    return {f"Name: {name}, Age: {age}, City:{city}"}

@app.get("/repeat")
def repeat(msg: str="hi", times: int=3):
    return {"result": [msg for _ in range(times)]}
        
@app.get("/fullname")
def fullname(first: str, last: str):
    return {"fullname": f"{first} {last}"}


@app.get("/upper")
def upper(text: str):
    return {"uppercase": text.upper()}


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
def nums(n: list[int]):
    return {"numbers": n}


@app.get("/substring")
def substring(text: str, start: int, end: int):
    return {"substring": text[start:end]}


@app.get("/checkpass")
def checkpass(pwd: str):
    return {"valid": len(pwd) >= 8}


@app.get("/temp")
def temp(c: float):
    f = (c * 9/5) + 32
    return {"celsius": c, "fahrenheit": f}


@app.get("/task/{task_name}")
def task_priority(task_name: str, priority: str = "normal"):
    return {"task": task_name, "priority": priority}


@app.get("/reverse")
def reverse(text: str):
    return {"reversed": text[::-1]}


@app.get("/mul/{a}")
def multiply(a: int, b: int):
    return {"product": a * b}

@app.get("/eligible")
def eligible(age: int):
    return {"eligible": age >= 18}
