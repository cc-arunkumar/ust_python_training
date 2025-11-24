from fastapi import FastAPI, Query

# Initialize FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

# Greet user by name (Path Parameter)
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hiiii Sugavano {name}!!!"}

# Add three numbers (Query Parameters)
@app.get("/add")
def add(a: int, b: int, c: int):
    return {"Sum is": f"{a+b+c}"}

# Square using Path Parameter
@app.get("/square/{number}")
def square(number: int):
    return {"Square is": f"{number**2}"}

# Square using Query Parameter
@app.get("/square")
def square(number: int):
    return {"Square is": f"{number**2}"}

# Check if number is even or odd
@app.get("/check/{num}")
def check(num: int):
    if num % 2 == 0:
        return {num: "is even"}
    else:
        return {num: "is odd"}

# User info with default city
@app.get("/user/{id}")
def user(id: int, city: str = "Mumbai"):
    return {id: city}

# Repeat a message multiple times
@app.get("/repeat")
def repeat(msg: str, times: int):
    return {"message": msg * times}

# Full name concatenation
@app.get("/fullname")
def repeat(first: str, last: str):
    return {"message": first + " " + last}

# Convert text to uppercase
@app.get("/upper")
def upper(text: str):
    return {"output": text.upper()}

# Calculate area of rectangle
@app.get("/area")
def area(length: int, breadth: int):
    return {"area": length * breadth}

# Age increment
@app.get("/age/{age}")
def age(age: int):
    return {"Next Year you will be": age + 1}

# Check if character exists in word
@app.get("/contains")
def contains(word: str, char: str):
    if char in word:
        return {"message": "Yes Found"}
    else:
        return {"message": "Not Found"}

# Movie details
@app.get("/movie/{movie}")
def movie(movie: str, year: int, rating: int):
    return {"output": f"{movie} was released in {year} with a rating of {rating}"}

# Accept list of numbers using Query
@app.get("/nums")
def nums(n: list[int] = Query(...)):
    return {"output": n}

# Extract substring
@app.get("/substring")
def substring(text: str, start: int, end: int):
    return {"output": text[start:end+1]}

# Check if password is non-empty
@app.get("/checkpass")
def checkpass(pwd: str):
    return {"output": True if len(pwd.strip()) != 0 else False}

# Convert Celsius to Fahrenheit
@app.get("/temp")
def temp(c: int):
    return {"Temperature in F": (c * 9 / 5) + 32}

# Task with priority
@app.get("/task/{task}")
def task(task: str, priority: str):
    return {"Output": f"{task} has a {priority} priority"}

# Reverse a string
@app.get("/reverse/{text}")
def reverse(text: str):
    return {"Reverse": text[::-1]}

# Multiply two numbers
@app.get("/multiply/{num1}")
def multiply(num1: int, num2: int):
    return {"product": num1 * num2}

# Check eligibility based on age
@app.get("/eligible/{age}")
def eligible(age: int):
    return {"eligible": True if age >= 18 else False}


# ---------------- SAMPLE INPUT & OUTPUT ----------------
"""
1. GET http://127.0.0.1:8000/
   Output: {"message": "Welcome to FastAPI"}

2. GET http://127.0.0.1:8000/greet/John
   Output: {"message": "Hiiii Sugavano John!!!"}

3. GET http://127.0.0.1:8000/add?a=2&b=3&c=4
   Output: {"Sum is": "9"}

4. GET http://127.0.0.1:8000/square/5
   Output: {"Square is": "25"}

5. GET http://127.0.0.1:8000/check/10
   Output: {10: "is even"}

6. GET http://127.0.0.1:8000/user/101?city=Pune
   Output: {101: "Pune"}

7. GET http://127.0.0.1:8000/repeat?msg=Hi&times=3
   Output: {"message": "HiHiHi"}

8. GET http://127.0.0.1:8000/fullname?first=John&last=Doe
   Output: {"message": "John Doe"}

9. GET http://127.0.0.1:8000/upper?text=hello
   Output: {"output": "HELLO"}

10. GET http://127.0.0.1:8000/area?length=5&breadth=4
    Output: {"area": 20}

11. GET http://127.0.0.1:8000/age/25
    Output: {"Next Year you will be": 26}

12. GET http://127.0.0.1:8000/contains?word=apple&char=p
    Output: {"message": "Yes Found"}

13. GET http://127.0.0.1:8000/movie/Inception?year=2010&rating=9
    Output: {"output": "Inception was released in 2010 with a rating of 9"}

14. GET http://127.0.0.1:8000/nums?n=1&n=2&n=3
    Output: {"output": [1, 2, 3]}

15. GET http://127.0.0.1:8000/substring?text=FastAPI&start=0&end=3
    Output: {"output": "Fast"}

16. GET http://127.0.0.1:8000/checkpass?pwd=hello
    Output: {"output": true}

17. GET http://127.0.0.1:8000/temp?c=0
    Output: {"Temperature in F": 32.0}

18. GET http://127.0.0.1:8000/task/Coding?priority=High
    Output: {"Output": "Coding has a High priority"}

19. GET http://127.0.0.1:8000/reverse/hello
    Output: {"Reverse": "olleh"}

20. GET http://127.0.0.1:8000/multiply/5?num2=4
    Output: {"product": 20}

21. GET http://127.0.0.1:8000/eligible/17
    Output: {"eligible": false}
"""