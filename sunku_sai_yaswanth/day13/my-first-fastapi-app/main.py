from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

# Simple hello world endpoint
@app.get("/")
def hello():
    return {"message": "Hello World, welcome to UST"}

# Greet user with an optional name (query param default)
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Good afternoon {name}"}

# Simple addition using query params
@app.get("/add")
def add(num1: int, num2: int, num3: int):
    return {"sum": num1 + num2 + num3}

# Get the square of a number (path param with default value)
@app.get("/square")
def square(num: int = 5):
    return {"square": num ** 2}

# Check if a number is even or odd (path param)
@app.get("/even_odd/{num}")
def even_odd(num: int):
    if num % 2 == 0:
        return {"message": f"{num} is even"}
    else:
        return {"message": f"{num} is odd"}

# User info with optional city (path + optional query)
@app.get("/user_info/{num}")
def user_info(num: int, city: str = "Mumbai"):
    return {f"user_number": num, "city": city}

# Repeat a message multiple times (query params)
@app.get("/repeat")
def repeat(msg: str, times: int):
    r = msg * times
    return {"message_repeated": r}

# Concatenate first and second name (query params)
@app.get("/name")
def name(first_name: str, second_name: str):
    return {"full_name": f"{first_name} {second_name}"}

# Convert a word to uppercase (query param)
@app.get("/upper")
def upper(word: str):
    name = word.upper()
    return {"in_upper_case": name}

# Calculate the area of a rectangle (query params for length and breadth)
@app.get("/rectangle")
def rectangle(l: int, b: int):
    return {"area_of_rectangle": l * b}

# Get the next age based on current age (path param)
@app.get("/next_age/{age}")
def next_age(age: int):
    return {"next_age": age + 1}

# Check if a character is in the given word (query params)
@app.get("/contains")
def contains(word: str, char: str):
    if char in word:
        return {"message": f"Character '{char}' is in the word '{word}'"}
    else:
        return {"message": f"Character '{char}' is not in the word '{word}'"}

# Movie details (path and query params)
@app.get("/movie/{word}")
def movie(word: str, year: int, rating: int):
    return {"movie": word, "year": year, "rating": rating}

# Accept a list of numbers (query param)
@app.get("/nums")
def list_num(n: list[int] = Query(...)):
    return {"list_of_numbers": n}

# Get a substring from the text (path params)
@app.get("/substring")
def sub_string(text: str, start: int, end: int):
    new = text[start:end]
    return {"substring": new}

# Validate password (length check)
@app.get("/checkpass")
def password(pwd: str):
    if len(pwd) == 7:
        return {"message": f"{pwd} is valid"}
    else:
        return {"message": f"{pwd} is not valid"}

# Temperature conversion: Celsius to Fahrenheit and vice versa (query params)
@app.get("/temp")
def temp(c: Optional[int] = None, f: Optional[int] = None):
    if c is not None:
        f = (c * 9/5) + 32
    elif f is not None:
        c = (f - 32) * 5/9
    return {"temp_in_celsius": c, "temp_in_fahrenheit": f}

# Task priority endpoint (query param)
@app.get("/task/clean-room")
def room_priority(priority: str):
    if priority == "high":
        return {"priority": "high"}
    elif priority == "medium":
        return {"priority": "medium"}
    else:
        return {"priority": "low"}

# Reverse the given word (query param)
@app.get("/reverse")
def word_reverse(text: str):
    rev = text[::-1]
    return {"reversed_word": rev}

# Multiply two numbers (path and query params)
@app.get("/mul/{num}")
def multiply(num: int, b: int):
    multi = num * b
    return {"multiply_result": multi}

# Check age eligibility (query param)
@app.get("/eligible")
def age_eligibility(age: int):
    if age >= 18:
        return {"eligibility": "Eligible"}
    else:
        return {"eligibility": "Not eligible"}
