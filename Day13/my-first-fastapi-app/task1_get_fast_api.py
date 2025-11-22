from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet(name:str):
    return{f"hello da",{name}}

@app.get("/square/{number}")
def square(number:int):
    return{f"square of value is:{number*number}"}


@app.get("/oddeven/{num}")
def oddeven(num: int):
    if num % 2 == 0:
        return {"result": "even"}
    else:
        return {"result": "odd"}
    
@app.get("/add")
def add(num:int):
    return{f"the square1 is : {num+num}"}
