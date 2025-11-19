from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

# Home route that returns a simple message
@app.get("/")
def home():
    return {"message": "Change in message"}

# Greet route that takes a name parameter and returns a greeting message
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello everyone {name}"}

# Another greet route that uses a query parameter to greet a person
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello everyone {name}"}

# Add route that accepts two integers and returns their sum
@app.get("/add")
def add(a: int, b: int):
    return {"sum=": a + b}

# Square route that calculates the square of a number provided in the URL
@app.get("/sqaure/{num}")
def square(num: int):
    return {"square:": f"{num ** 2}"} 

# Square route that calculates the square of a number with a default value of 10
@app.get("/square")
def sqaure(num1: int = 10):
    return {"square1:": num1 ** 2}   

# Check if a number is even or odd
@app.get("/check/{num}")
def check(num: int):
    if num % 2 == 0:
        return {"Even:", num}
    else:
        return {"Odd: ", num}

# Route that takes a number and city as input (defaults to "Hyderabad")
@app.get("/user/{num}")
def city(num: int, city: str = "Hyderabad"):
    return {"num": num, "city": city}

# Repeat a message a specified number of times
@app.get("/repeat")
def city(msg: str, times: int):
    r = msg * times
    return {"msg n times:": r}

# Combine first and last name to return a full name
@app.get("/fullname")
def fullname(first: str, last: str):
    full_name = first + last
    return {f"Full Name: {full_name}"}

# Convert the provided text to uppercase
@app.get("/upper")
def upper_case(text: str):
    text_upper = text.upper()
    return {f"text convert to upper case: {text_upper}"}

# Calculate the area of a rectangle given its length and width
@app.get("/area")
def area_of_rect(length: int, width: int):
    area = length * width
    return {"Area of Rectangle:": f"{area}"}

# Returns the age of the person next year
@app.get("/age/{num}")
def age(num: int):
    return {"Age next year": f"{num + 1}"}

# Check if a given character exists in the provided word
@app.get("/contains")
def char_contain(word: str, char: str):
    return {char in word}

# Movie rating endpoint that takes movie details as input
@app.get("/movie/{name}")
def rating(name: str, year: int, rating: int):
    return {
        "Movie name:": f"{name}",
        "Movie Year:": f"{year}",
        "Movie rating:": f"{rating}"
    }

# Accepts a list of numbers as query parameters and returns it
@app.get("/nums")
def list_num(n: list[int] = Query()):
    return {"list of n": n}

# Returns a substring of the given text from the start index to the end index
@app.get("/substring")
def substring_name(text: str, start: int, end: int):
    return {f"Substring of text: {text[start:end]}"}

# Check if the password has a length of at least 8 characters
@app.get("/checkpass")
def password_length(pwd: str):
    if len(pwd) >= 8:
        return {"Valid"}
    else:
        return {"Invalid"}

# Convert between Celsius and Fahrenheit temperatures
@app.get("/temp")
def get_temp(c: Optional[int] = None, f: Optional[int] = None):
    if c is not None:
        f = (c * 9 / 5) + 32  
    elif f is not None:
        c = (f - 32) * 5 / 9  

    return {"temp in c": c, "temp in f": f}

# Route to set room cleaning task priority
@app.get("/task/clean-room")
def room_priority(priority: str):
    if priority == "high":
        return {"priority is high"}
    elif priority == "medium":
        return {"priority is medium"}
    else:
        return {"priority is low"}

# Reverse the provided word
@app.get("/reverse")
def word_reverse(text: str):
    rev = text[::-1]
    return {f"Word reversing: {rev}"}

# Multiply two numbers
@app.get("/mul/{num}")
def multiply(num: int, b: int):
    multi = num * b
    return {f"multiply: {multi}"}

# Check if a person is eligible based on age (18 or older)
@app.get("/eligible")
def age_eligibility(age: int):
    if age >= 18:
        return {"Age if eligible"}
    else:
        return {"Age if Not eligible"}