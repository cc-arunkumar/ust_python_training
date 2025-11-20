from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Hyyyyyyy"}
# 1
@app.get("/greet/{name}")
def greet(name:str):
    return {"message" : f"{name}"}

# 4
@app.get("/add")
def add(a:int,b:int,c:int):
    return {"sum=":a+b+c}

# 2
@app.get("/square/{n}")
def square(n:int):
    return{"sq":n**2}

@app.get("/square")
def square(n:int=8):
    return{"sq":n**2}

# 3
@app.get("/check")
def evenodd(n:int):
    if n%2==0:
        return {"result": "Even"}
    else:
        return {"result":"Odd"}

# 8
@app.get("/upper")
def upper(text:str):
    return {"text":f"{text.upper()}"}

# 7
@app.get("/fullname")
def name(first:str,last:str):
    return {"first":f"{first}","last":f"{last}"}

# 9
@app.get("/area")
def rectangle(length:int,width:int):
    return {"length":f"{length}","width":f"{width}"}

# 5
@app.get("/user/{id}")
def user(id:int, city:str="Coimbatore"):
    return {"user_id": id, "city": city}

# 6
@app.get("/repeat")
def repeat(msg:str,n:int):
    return {"message": msg * n}

# 10
@app.get("/age/{current_age}")
def age(current_age:int):
    return {"age_next_year": current_age + 1}


# 11
@app.get("/contains")
def contains(word:str,char:str):
    return {"contains": char in word}

# 12
@app.get("/movie/{title}")
def movie(title:str,year:int=2009,rating:int=9):
    return {"title": title, "year": year, "rating": rating}

# 13
@app.get("/nums")
def nums(n: list[int]):
    return {"numbers": n}

# 14
@app.get("/substring")
def substring(text:str,start:int,end:int):
    return {"substring": text[start:end]}

# 15
@app.get("/checkpass")
def checkpass(pwd:str):
    return {"valid": len(pwd) >= 8}

# 16
@app.get("/temp")
def temp(c:float):
    return {"C": c, "F": (c * 9/5) + 32}

# 17
@app.get("/task/{name}")
def task(name:str,priority:str="low"):
    return {"task": name, "priority": priority}

# 18
@app.get("/reverse")
def reverse(text:str):
    return {"reversed": text[::-1]}

# 19
@app.get("/mul/{a}")
def mul(a:int,b:int):
    return {"product": a * b}

# 20
@app.get("/eligible")
def eligible(age:int):
    return {"eligible": age >= 18}


