from fastapi import FastAPI, Query

app = FastAPI()

# Home endpoint
@app.get("/")
def home():
    return {"message": "Hello Fastapi bye Fastapi + UV!"}

# Greet endpoint
@app.get("/greet")
def greet(name: str):
    return {"greet message": f"Hi {name} good afternoon"}  # Output: {"greet message":"Hi Akhil good afternoon"}

# Square endpoint
@app.get("/square/{num}")
def square(num: int):
    return {"square": f"{num**2}"}  # Output: {"square": "9"}

# Addition endpoint
@app.get("/add")
def add(a: int, b: int):
    return {"sum = ": a + b}  # Output: {"sum = ": 3}

# User details endpoint with optional city
@app.get("/user/{id}")
def user(id: int, city: str = "kerala"):  # Output: {"id": 24, "City": "kerala"}
    return {"id": id, "City": city}

# Repeat message endpoint
@app.get("/repeat")
def repeat(msg: str, times: int):  # Output: "akhilakhilakhil"
    return msg * times

# Full name endpoint
@app.get("/fullname")
def fullname(first: str, last: str):
    return {"Full name": first + " " + last}

# Convert string to uppercase
@app.get("/upper")
def upper(string: str):
    return {string: string.upper()}

# Area calculation endpoint
@app.get("/area")
def area(length: int, width: int):
    return {"Area": length * width}

# Age next year endpoint
@app.get("/age/{age}")
def age(age: int):
    return {"Next year age": age + 1}

# Check if character exists in word
@app.get("/contains")
def contains(word: str, char: str):
    return {"Contains": True if char in word else False}

# Movie details endpoint
@app.get("/movie/{name}")
def movie(name: str, year: int, rating: int):
    return {"Movie Name": name, "Year": year, "Rating": rating}

# Query list of numbers
@app.get("/num")
def num(n: list[int] = Query(...)):  # Output: {"n": [1, 2, 3]}
    return {"n": n}

# Substring extraction
@app.get("/substring")
def substring(text: str, start: int, end: int):
    return {"Substring": text[start:end]}

# Password length check
@app.get("/checkpass")
def checkpass(password: str):
    return {"CheckPass": True if len(password) == 8 else False}

# Temperature conversion
@app.get("/temp")
def temp(c: int):
    return {"C": c, "F": c * (9 / 5) + 32}

# Task details
@app.get("/task/name")
def task(name: str, priority: str):
    return {"Task": name, "Priority": priority}

# Reverse text endpoint
@app.get("/reverse")
def reverse(text: str):
    return {"Reverse": text[::-1]}

# Multiply two numbers
@app.get("/multiply/{a}")
def multiply(a: int, b: int):
    return {"mult": a * b}

# Age eligibility check
@app.get("/eligible")
def eligible(aage: int):
    return {"Age": aage, "Valid": True if aage >= 18 else False}

# Sample Output

"""
Sample Output for /greet (GET):
Input: /greet?name=Akhil
Output: {"greet message":"Hi Akhil good afternoon"}

Sample Output for /square/{num} (GET):
Input: /square/3
Output: {"square": "9"}

Sample Output for /add (GET):
Input: /add?a=1&b=2
Output: {"sum = ": 3}

Sample Output for /user/{id} (GET):
Input: /user/24?city=kerala
Output: {"id": 24, "City": "kerala"}

Sample Output for /repeat (GET):
Input: /repeat?msg=akhil&times=3
Output: "akhilakhilakhil"

Sample Output for /fullname (GET):
Input: /fullname?first=John&last=Doe
Output: {"Full name": "John Doe"}

Sample Output for /upper (GET):
Input: /upper?string=hello
Output: {"hello": "HELLO"}

Sample Output for /area (GET):
Input: /area?length=5&width=6
Output: {"Area": 30}

Sample Output for /age/{age} (GET):
Input: /age/25
Output: {"Next year age": 26}

Sample Output for /contains (GET):
Input: /contains?word=hello&char=e
Output: {"Contains": True}

Sample Output for /movie/{name} (GET):
Input: /movie/Inception?year=2010&rating=8
Output: {"Movie Name": "Inception", "Year": 2010, "Rating": 8}

Sample Output for /num (GET):
Input: /num?n=1&n=2&n=3
Output: {"n": [1, 2, 3]}

Sample Output for /substring (GET):
Input: /substring?text=hello&start=1&end=4
Output: {"Substring": "ell"}

Sample Output for /checkpass (GET):
Input: /checkpass?password=abcdefgh
Output: {"CheckPass": True}

Sample Output for /temp (GET):
Input: /temp?c=25
Output: {"C": 25, "F": 77.0}

Sample Output for /task/name (GET):
Input: /task/name?name=WriteReport&priority=High
Output: {"Task": "WriteReport", "Priority": "High"}

Sample Output for /reverse (GET):
Input: /reverse?text=hello
Output: {"Reverse": "olleh"}

Sample Output for /multiply/{a} (GET):
Input: /multiply/2?b=3
Output: {"mult": 6}

Sample Output for /eligible (GET):
Input: /eligible?aage=17
Output: {"Age": 17, "Valid": False}
"""
