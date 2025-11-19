# 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {"message" : "Hello World!"}

@app.get("/greet/{name}")
def greet(name:str):
    return{"msg" : f"hi {name}"}

@app.get("/add")
def add(a:int,b:int,c:int):
    return {"sum":a+b+c}

@app.get("/square")
def square(a:int):
    return {"square": a*a}

@app.get("/num")
def square(a:int=6):
    return {"square": a*a}

