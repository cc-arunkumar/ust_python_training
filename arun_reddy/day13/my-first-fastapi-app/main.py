# GET Tasks
# 1.Greet user with optional name (query param
# default)
# URL examples:
# /greet
# /greet?name=rahul
# 2.Get square of a number (path param)
# URL: /square/7
# 3.Check if number is even or odd (path)
# /check/12
# 4.Simple addition using query params
# /add?a=10&b=5
# 5.User info with optional city (path + optional query)
# /user/24
# /user/24?city=Mumbai
# 6.Repeat a message n times
# /repeat?msg=hi&times=3
# 7.Full name using two query parameters
# /fullname?first=rahul&last=sharma
# 8.Convert string to uppercase
# GET Tasks 1
# /upper?text=hello
# 9.Calculate area of rectangle
# /area?length=5&width=3
# 10.Age next year
# /age/24
# 11.Check if a word contains a character
# /contains?word=hello&char=l
# 12.Combine path + multiple query params
# /movie/Avatar?year=2009&rating=9
# 13.Return list of numbers sent(query repeats)
# /nums?n=1&n=2&n=3
# 14.Show substring of a string
# /substring?text=hello&start=1&end=4
# 15.Validate password length
# /checkpass?pwd=abcd1234
# 16.Gettemperature in C and F
# /temp?c=30
# 17.Path + query:task with priority
# /task/clean-room?priority=high
# 18.Reverse text
# GET Tasks 2
# /reverse?text=hello
# 19.Multiply 2 numbers (path + query)
# /mul/10?b=5
# 20.Check age eligibility
# /eligible?age=17
# GET Tasks 3


from fastapi import FastAPI, Query
from typing import List

# Initialize FastAPI application
app = FastAPI(title="UST Demo API")

# -------------------------------
# Root endpoint
# -------------------------------
@app.get("/")
def home():
    """
    Root endpoint.
    Returns a simple welcome message.
    """
    return {"message": "Hello FastAPI + UVI"}   # Example response


# -------------------------------
# Greeting endpoint (path parameter)
# -------------------------------
@app.get("/greet/{yashu}")
def greet(yashu: str):
    """
    Greets a user using a path parameter.
    Example: /greet/Asha -> "Gud Afternoon Asha"
    """
    return {"message": f"Gud Afternoon {yashu}"}


# -------------------------------
# Addition endpoint (query parameters)
# -------------------------------
@app.get("/add")
def add(num1: int, num2: int, num3: int):
    """
    Adds three numbers passed as query parameters.
    Example: /add?num1=1&num2=2&num3=3 -> {"sum": 6}
    """
    return {"sum": num1 + num2 + num3}


# -------------------------------
# Square endpoint (path parameter)
# -------------------------------
@app.get("/square/{num}")
def square(num: int):
    """
    Returns the square of a number using path parameter.
    Example: /square/4 -> {"square": 16}
    """
    return {"square": num ** 2}


# -------------------------------
# Square endpoint (query parameter)
# -------------------------------
@app.get("/square")
def square(num: int):
    """
    Returns the square of a number using query parameter.
    Example: /square?num=5 -> {"square": 25}
    """
    return {"square": num ** 2}


# -------------------------------
# Greeting endpoint (query parameter)
# -------------------------------
@app.get("/greet")
def greet(name: str):
    """
    Greets a user using query parameter.
    Example: /greet?name=Asha -> {"message": "welcome Asha"}
    """
    return {"message": f"welcome {name}"}


# -------------------------------
# Even/Odd check
# -------------------------------
@app.get("/check/{num}")
def check(num: int):
    """
    Checks if a number is even or odd.
    Example: /check/4 -> {"message": "4 is even"}
    """
    if num % 2 == 0:
        return {"message": f"{num} is even"}
    else:
        return {"message": f"{num} is odd"}


# -------------------------------
# User info endpoint
# -------------------------------
@app.get("/user/{id}")
def user_info(id: int, city: str = "UNKNOWN"):
    """
    Returns user ID and city.
    Example: /user/10?city=Pune -> {"message": "User ID: 10 City: Pune"}
    """
    return {"message": f"User ID: {id} City: {city}"}


# -------------------------------
# Repeat message (prints to console)
# -------------------------------
@app.get("/repeat")
def repeat(msg: str, times: int):
    """
    Prints a message multiple times to the console.
    Example: /repeat?msg=Hi&times=3 -> prints "Hi" three times
    """
    for _ in range(times):
        print(msg)
    return {"message": f"Message '{msg}' repeated {times} times in console"}


# -------------------------------
# Full name
# -------------------------------
@app.get("/fullname")
def fullname(first: str, last: str):
    """
    Combines first and last name.
    Example: /fullname?first=Asha&last=Rao -> {"Full Name": "Asha Rao"}
    """
    return {"Full Name": f"{first} {last}"}


# -------------------------------
# Uppercase text
# -------------------------------
@app.get("/upper")
def upper(text: str):
    """
    Converts text to uppercase.
    Example: /upper?text=hello -> {"Text in Upper Case": "HELLO"}
    """
    return {"Text in Upper Case": text.upper()}


# -------------------------------
# Area calculation
# -------------------------------
@app.get("/area")
def area(length: int, width: int):
    """
    Calculates area of a rectangle.
    Example: /area?length=5&width=4 -> {"Area": 20}
    """
    return {"Area": length * width}


# -------------------------------
# Age endpoint
# -------------------------------
@app.get("/age/{age}")
def age(age: int):
    """
    Returns the age provided.
    Example: /age/25 -> {"Age": 25}
    """
    return {"Age": age}


# -------------------------------
# Contains check
# -------------------------------
@app.get("/contains")
def contains(word: str, char: str):
    """
    Checks if a character is present in a word.
    Example: /contains?word=hello&char=e -> {"message": "e is present in hello"}
    """
    if char in word:
        return {"message": f"{char} is present in {word}"}
    else:
        return {"message": f"{char} is not present in {word}"}


# -------------------------------
# Movie info
# -------------------------------
@app.get("/movie/{name}")
def movie(name: str, year: int, rating: int):
    """
    Returns movie details.
    Example: /movie/Inception?year=2010&rating=9 -> {"Movie": "Inception | Year: 2010 | Rating: 9"}
    """
    return {"Movie": f"{name} | Year: {year} | Rating: {rating}"}


# -------------------------------
# Numbers list
# -------------------------------
@app.get("/nums")
def nums(n: List[int] = Query(...)):
    """
    Accepts a list of numbers.
    Example: /nums?n=1&n=2&n=3 -> {"List of numbers": [1, 2, 3]}
    """
    return {"List of numbers": n}


# -------------------------------
# Substring
# -------------------------------
@app.get("/substring")
def substring(text: str, start: int, end: int):
    """
    Returns substring of text.
    Example: /substring?text=hello&start=1&end=4 -> {"Substring": "ell"}
    """
    return {"Substring": text[start:end]}


# -------------------------------
# Password check
# -------------------------------
@app.get("/checkpass")
def checkpass(pwd: str):
    """
    Validates password length.
    Example: /checkpass?pwd=abcdefgh -> {"message": "Password Success"}
    """
    if len(pwd) > 8:
        return {"message": "Password Success"}
    else:
        return {"message": "Password must contain minimum 8 characters"}


# -------------------------------
# Temperature conversion
# -------------------------------
@app.get("/temp")
def temp(c: int):
    """
    Converts Celsius to Fahrenheit.
    Example: /temp?c=0 -> {"Temperature in Fahrenheit": 32.0}
    """
    return {"Temperature in Fahrenheit": (9/5) * c + 32}


# -------------------------------
# Task endpoint
# -------------------------------
@app.get("/task/{clean_room}")
def task(clean_room: int, priority: str):
    """
    Returns task details.
    Example: /task/101?priority=High -> {"Task": "Clean Room no: 101 | Priority: High"}
    """
    return {"Task": f"Clean Room no: {clean_room} | Priority: {priority}"}


# -------------------------------
# Reverse text
# -------------------------------
@app.get("/reverse")
def reverse(text: str):
    """
    Reverses the given text.
    Example: /reverse?text=hello -> {"Reversed": "olleh"}
    """
    return {"Reversed": text[::-1]}


# -------------------------------
# Multiplication
# -------------------------------
@app.get("/mul/{num1}")
def mul(num1: int, num2: int):
    """
    Multiplies two numbers.
    Example: /mul/5?num2=4 -> {"Product": 20}
    """
    return {"Product": num1 * num2}


# -------------------------------
# Eligibility check
# -------------------------------
@app.get("/eligible")
def eligible(age: int):
    """
    Checks if age is eligible (>18).
    Example: /eligible?age=20 -> {"message": "You are Eligible"}
    """
    if age > 18:
        return {"message": "You are Eligible"}
    else:
        return {"message": "Age below 18"}


# ouput for each endpoints
# 1. Root Endpoint
# Request:
# GET /
# Response:
# {
#   "message": "Hello FastAPI + UVI"
# }

# 2. Greeting (path parameter)
# Request:
# GET /greet/Asha
# Response:
# {
#   "message": "Gud Afternoon Asha"
# }

# 3. Addition (three numbers)
# Request:
# GET /add?num1=2&num2=3&num3=4
# Response:
# {
#   "sum": 9
# }

# 4. Square (path parameter)
# Request:
# GET /square/5
# Response:
# {
#   "square": 25
# }

# 5. Square (query parameter)
# Request:
# GET /square?num=6
# Response:
# {
#   "square": 36
# }

# 6. Greeting (query parameter)
# Request:
# GET /greet?name=Meera
# Response:
# {
#   "message": "welcome Meera"
# }

# 7. Even/Odd Check
# Request:
# GET /check/7
# Response:
# {
#   "message": "7 is odd"
# }

# 8. User Info
# Request:
# GET /user/10?city=Pune
# Response:
# {
#   "message": "User ID: 10 City: Pune"
# }

# 9. Full Name
# Request:
# GET /fullname?first=Asha&last=Rao
# Response:
# {
#   "Full Name": "Asha Rao"
# }

# 10. Uppercase Text
# Request:
# GET /upper?text=hello
# Response:
# {
#   "Text in Upper Case": "HELLO"
# }

# 11. Area Calculation
# Request:
# GET /area?length=5&width=4
# Response:
# {
#   "Area": 20
# }

# 12. Age Endpoint
# Request:
# GET /age/25
# Response:
# {
#   "Age": 25
# }

# 13. Contains Check
# Request:
# GET /contains?word=hello&char=e
# Response:
# {
#   "message": "e is present in hello"
# }

# 14. Movie Info
# Request:
# GET /movie/Inception?year=2010&rating=9
# Response:
# {
#   "Movie": "Inception | Year: 2010 | Rating: 9"
# }

# 15. Numbers List
# Request:
# GET /nums?n=1&n=2&n=3
# Response:
# {
#   "List of numbers": [1, 2, 3]
# }

# 16. Substring
# Request:
# GET /substring?text=hello&start=1&end=4
# Response:
# {
#   "Substring": "ell"
# }

# 17. Password Check
# Request:
# GET /checkpass?pwd=abcdefghij
# Response:
# {
#   "message": "Password Success"
# }

# 18. Temperature Conversion
# Request:
# GET /temp?c=0
# Response:
# {
#   "Temperature in Fahrenheit": 32.0
# }

# 19. Task Endpoint
# Request:
# GET /task/101?priority=High
# Response:
# {
#   "Task": "Clean Room no: 101 | Priority: High"
# }

# 20. Reverse Text
# Request:
# GET /reverse?text=hello
# Response:
# {
#   "Reversed": "olleh"
# }

# 21. Multiplication
# Request:
# GET /mul/5?num2=4
# Response:
# {
#   "Product": 20
# }

# 22. Eligibility Check
# Request:
# GET /eligible?age=20
# Response:
# {
#   "message": "You are Eligible"
# }