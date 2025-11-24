from fastapi import FastAPI, Query
from typing import List

# FastAPI app initialization
app = FastAPI()

# Endpoint to greet a user by their name.
# Takes 'name' as a path parameter and returns a greeting message.
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hi {name}"}

# Endpoint to calculate the square of a given number.
# Takes 'num' as a path parameter and returns the square of the number.
@app.get("/square/{num}")
def square(a: int):
    return {"message": f"The square is {a*a}"}

# Endpoint to check if a number is even or odd.
# Takes 'num' as a path parameter and returns whether the number is even or odd.
@app.get("/is_even_or_odd/{num}")
def is_even_or_odd(a: int):
    if a % 2 == 0:
        return {"message": "even"}
    else:
        return {"message": "odd"}

# Endpoint to calculate the sum of two numbers.
# Takes two integers, 'a' and 'b', as query parameters and returns their sum.
@app.get("/calc_sum/{a}")
def calc_sum(a: int, b: int):
    return {"message": f"Sum is {a + b}"}

# Endpoint to fetch user information based on user_id and an optional city parameter.
# Returns user_id and city (if provided).
@app.get("/user/{user_id}")
def user_info(user_id: int, city: str = None):
    if city:
        return {"user_id": user_id, "city": city}
    return {"user_id": user_id}

# Endpoint to repeat a message multiple times.
# Takes 'msg' and 'num' as parameters, and returns the message repeated 'num' times.
@app.get("/repeat/{msg}")
def repeat(msg: str, num: int):
    result = [msg] * num
    return {"message": result}

# Endpoint to concatenate two names into a single string.
# Takes 'first' and 'last' as parameters and returns the concatenated names.
@app.get("/two_names/{first}")
def two_names(first: str, last: str):
    return {"message": first + last}

# Endpoint to convert a given string to uppercase.
# Takes a string 'string' as a query parameter and returns the string in uppercase.
@app.get("/to_upper")
def to_upper(string: str):
    return {"message": string.upper()}

# Endpoint to calculate the area of a rectangle.
# Takes 'length' and 'breadth' as query parameters and returns the area.
@app.get("/calc_area")
def calc_area(length: int, breadth: int):
    return {"message": f"Area is {length * breadth}"}

# Endpoint to calculate a person's age next year.
# Takes 'age' as a query parameter and returns the age next year.
@app.get("/age_next_year")
def age_next_year(age: int):
    return {"message": f"Age next year is {age + 1}"}

# Endpoint to check if a given character is present in a word.
# Takes 'word' and 'character' as parameters and returns True or False.
@app.get("/word_contains")
def word_contains(word: str, character: str):
    return {"result": character in word}

# Endpoint to get movie details by name, year, and rating.
# Takes 'movie_name', 'year', and 'rating' as parameters and returns the movie details.
@app.get("/get_movie/{movie_name}")
def get_movie(movie_name: str, year: int, rating: int):
    return {
        "movie": movie_name,
        "year": year,
        "rating": rating
    }

# Endpoint to receive a list of numbers as a query parameter and return them.
# Uses Query to accept a list of numbers.
@app.get("/nums")
def get_nums(n: List[int] = Query(...)):
    return {"numbers": n}

# Endpoint to extract a substring from a string.
# Takes 'string', 'start', and 'end' as parameters and returns the substring.
@app.get("/show_substring")
def show_substring(string: str, start: int, end: int):
    result = string[start:end+1]
    return {"message": result}

# Endpoint to check if a password matches a specified length.
# Takes 'pwd' and 'length' as parameters and checks if the password length matches.
@app.get("/checkpass")
def checkpass(pwd: str, length: int):
    return {"message": len(pwd) == length}

# Endpoint to convert a temperature from Celsius to Fahrenheit.
# Takes a temperature in Celsius as a query parameter and returns the Fahrenheit equivalent.
@app.get("/tempretaure")
def tempretaure(temp: float):
    f = (temp * 9 / 5) + 32
    return {
        "Celsius": temp,
        "Fahrenheit": f
    }

# Endpoint to get task details.
# Takes 'task_name' and 'priority' as parameters and returns the task with its priority.
@app.get("/get_task/{task_name}")
def get_task(task_name: str, priority: str):
    return {
        "Task": task_name,
        "Priority": priority
    }

# Endpoint to reverse the given text.
# Takes 'text' as a query parameter and returns the reversed text.
@app.get("/reverse")
def reverse(text: str):
    return {"Reversed Text": text[::-1]}

# Endpoint to multiply two numbers.
# Takes 'a' and 'b' as parameters and returns the result of a * b.
@app.get("/multiply/{a}")
def multiply(a: int, b: int):
    return {"Multiplication": a * b}

# Endpoint to check age eligibility based on a threshold.
# Takes 'age' as a parameter and checks if the person is older than 18.
@app.get("/check_age_eligiblity")
def check_age_eligiblity(age: int):
    if age <= 18:
        return {"Age Requirements": "Not Met"}
    return {"Age Requirements": "Met"}
