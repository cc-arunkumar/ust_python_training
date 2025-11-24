from fastapi import FastAPI

app = FastAPI()

# Home endpoint
@app.get("/")
def home():
    return {"message": "Hello Fastapi bye Fastapi + UV!"}

# Greet endpoint with a path parameter
@app.get("/greet/{name}")
def greet(name: str):
    return {"greet message": f"Hi {name} good afternoon"}

# Addition endpoint with three query parameters
@app.get("/add")
def add(a: int, b: int, c: int): 
    print("--------> Add called")
    return {"sum = ": a + b + c}

# Square of a number using path parameter
@app.get("/square/{num}")
def square(num: int): 
    return {"square": f"{num**2}"}

# Square of a number using a query parameter (default value is 5)
@app.get("/square")
def square(num: int = 5): 
    return {"square": f"{num**2}"}

# Endpoint to return a list of numbers
@app.get("/user")
def user(n: list[int]):
    return n

# Sample Output

"""
Sample Output for / (GET):
Output:
{
    "message": "Hello Fastapi bye Fastapi + UV!"
}

Sample Output for /greet/{name} (GET):
Input: /greet/Akhil
Output:
{
    "greet message": "Hi Akhil good afternoon"
}

Sample Output for /add (GET):
Input: /add?a=1&b=2&c=3
Output:
{
    "sum = ": 6
}

Sample Output for /square/{num} (GET):
Input: /square/4
Output:
{
    "square": "16"
}

Sample Output for /square (GET):
Input: /square?num=7
Output:
{
    "square": "49"
}

Sample Output for /user (GET):
Input: /user?n=1&n=2&n=3
Output:
[1, 2, 3]
"""
