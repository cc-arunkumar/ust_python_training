
from  fastapi import FastAPI

app = FastAPI()
# @app.get("/")
# def home():
#     return {"message" : "Hello FastAPI + UV!"}

# @app.get("/add")
# def add(num : int , num2 : int , num3 : int):
#     return {"sum = " : num + num2 + num3}

# @app.get("/greet/{name}")
# def greet():
#     return {"message " : f" Good afternoon {"Sohan"}"}


# @app.get("/square")
# def sq(num : int):
#     return {"Square = " : num * num}

# @app.get("/square/{num}")
# def squ (num : int):
#     return {"Square =" : num * num}



#Task : GET Question
#1
@app.get("/greet")
def greet():
    return {f" Good afternoon Sohan"}


#2
@app.get("/power")
def power(num: int, exp: int = 2):
    return {"result": num ** exp}


#3
@app.get("/even")
def even(num: int):
    return { "Even " : num % 2==0}

#4
@app.get("/add")
def add(num : int , num2 : int , num3 : int):
    return {"sum = " : num + num2 + num3}

#5
@app.get("/greet/{name}")
def optional (name : str , city : str="Mumbai"):
    return {"message : " : f" Hello {name } welcome to {city}"}

#6
@app.get("/repeat")
def message(msg: str="hello", times:int=3):
    return {"result": [msg for _ in range(times)]}

#Output
# {"result":["hello","hello","hello"]}

#7
@app.get("/fullname")
def fullname(first : str="Sohan", last : str="Rout"):
    return {f"Fullname : {first} {last}"}

#Output
# ["Fullname : Sohan Rout"]

#8
@app.get("/upper")
def upper(text : str):
    return {"uppercase" : text.upper()}

#Output
# {"uppercase":"HELLO"}

#9
@app.get("/area")
def area (length : float , width: float):
    return {"area ": length * width}

#10
@app.get("/age/{age}")
def age_next(age: int):
    return {"next_year_age": age + 1}

# 11 
@app.get("/contains")
def contains(word: str, char: str):
    return {"contains": char in word}

# 12 
@app.get("/movie/{title}")
def movie(title: str, year: int, rating: int):
    return {"title": title, "year": year, "rating": rating}
#14
@app.get("/substring")
def substring(text: str, start: int, end: int):
    return {"substring": text[start:end]}

#15
@app.get("/checkpass")
def checkpass(pwd: str):
    return {"valid": len(pwd) >= 8}

#16
@app.get("/temp")
def temp(c: float):
    return {"Celsius": c, "Fahrenheit": (c * 9/5) + 32}
#17
@app.get("/task/{taskname}")
def task(taskname: str, priority: str = "normal"):
    return {"task": taskname, "priority": priority}
#18
@app.get("/reverse")
def reverse(text: str):
    return {"reversed": text[::-1]}
#19
@app.get("/mul/{a}")
def mul(a: int, b: int):
    return {"product": a * b}
#20
@app.get("/eligible")
def eligible(age: int):
    return {"eligible": age >= 18}




