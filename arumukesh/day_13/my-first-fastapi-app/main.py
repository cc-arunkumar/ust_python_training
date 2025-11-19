from fastapi import FastAPI, Query
from typing import List

# Creating a FastAPI application instance
app = FastAPI()

# Greeting endpoint: takes a name as a URL parameter and returns a greeting message
@app.get("/greet/{name}")
def greet(name: str):
    return {"msg": f"hello {name}"}  # Returns a greeting message with the provided name

# Home endpoint: Returns a simple welcome message
@app.get("/")
def home():
    return {"message": "Hellow FAstAPI +UV"}  # Simple homepage message

# Add two numbers: Takes two query parameters (num1 and num2) and returns their sum
@app.get("/add")
def add(num1: int = 2, num2: int = 2):  # Default values of 2 for both numbers
    return {"sum=": num1 + num2}  # Returns the sum of the two numbers

# Square of a number: Takes a number as a path parameter and returns its square
@app.get("/square/{num}")
def square(num: int):
    return {"square=": num ** 2}  # Returns the square of the number

# Check if a number is odd or even: Takes a number as a path parameter and checks if it's odd or even
@app.get("/check_odd_eve/{num}")
def check_odd_eve(num: int):
    if num % 2 == 0:
        return {f"{num} is even"}  # Returns if the number is even
    else:
        return {f"{num} is odd"}  # Returns if the number is odd

# User info: Takes a number as a path parameter and an optional city as a query parameter
@app.get("/user_info/{num}")
def user_info(num: int, city: str = ""):
    return {f"{num} is the number and city is {city}"}  # Returns user number and city info

# Repeat a message: Takes a message and the number of times to repeat it as query parameters
@app.get("/repeat")
def repeat(msg: str, times: int):
    return {times * msg}  # Returns the message repeated the specified number of times

# Fullname: Takes first and last names as query parameters and concatenates them
@app.get("/fullname")
def fullname(f_name: str, last_name: str):
    return {f_name + last_name}  # Returns the full name (first + last)

# Convert to uppercase: Takes a string and converts it to uppercase
@app.get("/upper")
def upper(text: str):
    return {text.upper()}  # Returns the uppercase version of the provided text

# Calculate area: Takes length and width as query parameters and returns the area (length * width)
@app.get("/area")
def area(l: int, w: int):
    return {l * w}  # Returns the area of a rectangle

# Increment age by 1: Takes age as a path parameter and returns the next age (age + 1)
@app.get("/age_next/{num}")
def area(age: int):  # Function name 'area' is misleading here
    return {age + 1}  # Returns the next age

# Check if a character exists in a string: Takes a word and a character as query parameters and checks if the character exists in the word
@app.get("/check_char")
def check_char(word: str, char: str):
    if char in word:
        return {f"{char} exists in {word}"}  # Returns if character exists in the word
    else:
        return {f"{char} is not in {word}"}  # Returns if character does not exist in the word

# Movie info: Takes movie name, year, and rating as query parameters and returns them in a formatted string
@app.get("/movie/{name}")
def movie(name: str, year: int, rating: int):
    return {f"movie:{name}|year:{year}|rating:{rating}"}  # Returns movie details

# Get a list of numbers: Takes a list of integers as a query parameter
@app.get("/nums")
def nums(n: List[int] = Query(...)):  # The ... means this parameter is required
    return n  # Returns the list of numbers

# Extract a substring: Takes a string and two integers (start and end) as query parameters to slice the string
@app.get("/substring")
def substring(text: str, start: int, end: int):
    return text[start:end]  # Returns the substring from start to end index

# Check password length: Takes a password as a query parameter and checks if its length is greater than 5
@app.get("/checkpass")
def checkpass(pwd: str):
    if len(pwd) > 5:
        return {"passed!"}  # Returns a success message if the password length is greater than 5
    else:
        return {"not enough length"}  # Returns a failure message if the password is too short

# Convert temperature: Takes a temperature in Celsius and converts it to Fahrenheit
@app.get("/temp")
def temp(c: int):
    return {f"Fahrenheit: {c * 9 / 5 + 32}"}  # Returns the converted Fahrenheit temperature

# Multiply two numbers: Takes two integers and returns their product
@app.get("/mul")
def mul(a: int, b: int):
    return {a * b}  # Returns the product of the two numbers

# Eligibility check: Takes an age and checks if the person is eligible (over 17 years old)
@app.get("/eligible")
def eligible(age: int):
    if age > 17:
        return {"ok"}  # Returns success if eligible
    else:
        return {"not eligible"}  # Returns failure if not eligible
