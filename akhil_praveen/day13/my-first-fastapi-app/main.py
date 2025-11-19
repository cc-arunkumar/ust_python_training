from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello Fastapi bye Fastapi + UV!"}

@app.get("/greet/{name}")
def greet(name:str):
    return {"greet message":f"Hi {name} good afternoon"}

@app.get("/add")
def add(a:int,b:int,c:int): 
    print("--------> Add called")
    return {"sum = " : a + b + c}

@app.get("/square/{num}")
def square(num:int): 
    return {"square " : f"{num**2}"}

@app.get("/square")
def square(num:int=5): 
    return {"square " : f"{num**2}"}

@app.get("/user")
def user(n:list[int]):
    return n