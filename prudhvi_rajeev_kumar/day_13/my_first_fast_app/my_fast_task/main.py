from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{name}")
def greet(name : str):
    return {"message" : f"Hi {name}"}

@app.get("/square/{num}")
def square(a:int):
    return {"message" : f"The square is {a*a}"}

@app.get("/is_even_or_odd/{num}")
def is_even_or_odd(a:int):
    if a % 2 == 0:
        return {"message" : "even"}
    else:
        return{"message" : "odd"}
    
@app.get("/calc_sum")
def calc_sum(a:int, b:int):
    return {"message" : f"Sum is {a+b}"}

@app.get("/optional_city")
def optional_city(city : str):
    return {"message" : f"City -> {city}" or ""}


