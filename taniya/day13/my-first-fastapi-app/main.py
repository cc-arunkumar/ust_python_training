from typing import List
from fastapi import FastAPI, Query

# Create FastAPI app instance
app = FastAPI()

# -------------------------------
# Root endpoint
# -------------------------------
@app.get("/")
def home():
    return {"message": "Hello Fast API + UV! hiiiii hey"}
# Sample output: {"message": "Hello Fast API + UV! hiiiii hey"}

# -------------------------------
# Greeting endpoint
# -------------------------------
@app.get("/greet")
def greet(name: str = "taniya"):
    return {"message": f"Good Afternoon {name}"}
# Sample output: {"message": "Good Afternoon Taniya"}

# -------------------------------
# Addition endpoint
# -------------------------------
@app.get("/add")
def add(num1: int, num2: int, num3: int):
    return {"sum": num1 + num2 + num3}
# Sample output: {"sum": 9}

# -------------------------------
# Subtraction endpoint
# -------------------------------
@app.get("/sub")
def sub(num1: int, num2: int):
    return {"sub": num1 - num2}
# Sample output: {"sub": 7}

# -------------------------------
# Square endpoint (path parameter)
# -------------------------------
@app.get("/square/{num}")
def square_path(num: int):
    return {"square": num * num}
# Sample output: {"square": 36}

# -------------------------------
# Square endpoint (query parameter with default)
# -------------------------------
@app.get("/square")
def square_query(num: int = 25):
    return {"square": num * num}
# Sample output: {"square": 64}

# -------------------------------
# Even/Odd check endpoint
# -------------------------------
@app.get("/number")
def check(num: int):
    return {"result": "even" if num % 2 == 0 else "odd"}
# Sample output: {"result": "odd"}

# -------------------------------
# User endpoint with default values
# -------------------------------
@app.get("/user")
def user(id: int = 24, city: str = "Mumbai"):
    return {"id": id, "city": city}
# Sample output: {"id": 101, "city": "Pune"}

# -------------------------------
# Repeat message endpoint
# -------------------------------
@app.get("/repeat")
def repeat(msg: str, times: int):
    return {"result": " ".join([msg] * times)}
# Sample output: {"result": "Hi Hi Hi"}

# -------------------------------
# Name combine endpoint
# -------------------------------
@app.get("/name")
def name(first_name: str, last_name: str):
    return {"full_name": f"{first_name} {last_name}"}
# Sample output: {"full_name": "Alice Smith"}

# -------------------------------
# Uppercase conversion endpoint
# -------------------------------
@app.get("/upper")
def upper(word: str):
    return {"uppercase": word.upper()}
# Sample output: {"uppercase": "HELLO"}

# -------------------------------
# Area calculation endpoint
# -------------------------------
@app.get("/area")
def area(length: int, width: int):
    return {"area": length * width}
# Sample output: {"area": 20}

# -------------------------------
# Age increment endpoint
# -------------------------------
@app.get("/age")
def age(age: int):
    return {"Age next year": age + 1}
# Sample output: {"Age next year": 26}

# -------------------------------
# Contains check endpoint
# -------------------------------
@app.get("/contains")
def contains(word: str, char: str):
    return {"result": char in word}
# Sample output: {"result": true}

# -------------------------------
# Movie combine endpoint
# -------------------------------
@app.get("/combine")
def combine(movie: str, year: int, rating: int):
    return {"movie": movie, "year": year, "rating": rating}
# Sample output: {"movie": "Inception", "year": 2010, "rating": 9}

# -------------------------------
# Numbers list endpoint
# -------------------------------
@app.get("/numss")
def numss(n: List[int] = Query(...)):
    return {"numbers": n}
# Sample output: {"numbers": [1, 2, 3]}

# -------------------------------
# Substring endpoint
# -------------------------------
@app.get("/substring")
def substring(text: str, first: int, last: int):
    return {"substring": text[first:last]}
# Sample output: {"substring": "Fast"}

# -------------------------------
# Password validation endpoint
# -------------------------------
@app.get("/password")
def password(pswd: str):
    if len(pswd) >= 10:
        return {"valid": True}
    else:
        return {"valid": False, "reason": "Password must be at least 10 characters"}
# Sample output: {"valid": True}

# -------------------------------
# Temperature conversion endpoint
# -------------------------------
@app.get("/temp")
def temp(c: float):
    f = (c * 9 / 5) + 32
    return {"celsius": c, "fahrenheit": f}
# Sample output: {"celsius": 25, "fahrenheit": 77.0}

# -------------------------------
# Task endpoint
# -------------------------------
@app.get("/task")
def task(task: str, priority: int):
    return {"task": task, "priority": priority}
# Sample output: {"task": "WriteCode", "priority": 1}

# -------------------------------
# Reverse word endpoint
# -------------------------------
@app.get("/reverse")
def reverse(word: str):
    return {"reverse word": word[::-1]}
# Sample output: {"reverse word": "olleh"}

# -------------------------------
# Multiplication endpoint
# -------------------------------
@app.get("/mul")
def multiply(a: int, b: int):
    return {"result": a * b}
# Sample output: {"result": 42}

# -------------------------------
# Eligibility check endpoint
# -------------------------------
@app.get("/eligible")
def eligible(age: int):
    return {"eligible": age >= 18}
# Sample output: {"eligible": true}