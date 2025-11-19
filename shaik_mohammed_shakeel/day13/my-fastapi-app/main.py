from fastapi import FastAPI, Query

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello Shakeel"}
@app.get("/greet/{name}")
def greet(name:str):
    return {"message": f"Good Afternoon{name}"}

@app.get("/add")
def add(num1:int,num2:int,num3:int):
    return{"sum=":num1+num2+num3}

@app.get("/square")
def square(num:int=5):
    return{"Square=":num*num}

# 3.Check if number is even or odd (path)

@app.get("/even/{num}")
def even(num:int):
    if num%2==0:
        return{"Even":num}
    else:
        return{"odd":num}
    
# 4.Simple addition using query params
@app.get("/add")
def add(num1:int,num2:int,num3:int):
    return{"sum=":num1+num2+num3}

# 5.User info with optional city (path + optional query)
@app.get("/city/{num}")
def city(num:int,name:str = "Mumbai"):
    return {f"num":{num},"city":{name}}

# 6.Repeat a message n times
@app.get("/repeat")
def repeat(msg:str,times:int):
    return{f"message":{msg*times}}

# 7.Full name using two query parameters
@app.get("/fullname")
def fullname(msg1:str,msg2:str):
    return{"Full name":f"{msg1},{msg2}"}

# 8.Convert string to uppercase
@app.get("/upper")
def upper(text:str):
    a=text.upper()
    return{"Changes to upper":f"{a}"}

# 9.Calculate area of rectangle
@app.get("/area")
def area(l:int,b:int):
    return{"Area of Rectangle":{l*b}}

# 10.Age next year
@app.get("/nextage/{age}")
def nextage(age:int):
    return{"Next Year Age":{age+1}}

# 11.Check if a word contains a character
@app.get("/check")
def check(word:str,letter:str):
    for i in word:
        if i==letter:
            return{"Contains"}
        
# 12.Combine path + multiple query params

@app.get("/movie/{title}")
def get_movie(title: str, year: int, rating: int):
    return {"Movie Title": title,"Year": year,"Rating": rating}

#13.Return list of numbers sent(query repeats)
@app.get("/nums")
def list_num(n: list[int] = Query()):
    return {"list of n": n}
            
# 14. Show substring of a string
@app.get("/substring")
def substring(text: str, start: int, end: int):
    return {"substring": text[start:end]}

# 15. Validate password length
@app.get("/checkpass")
def checkpass(pwd: str):
    return {"valid": len(pwd) >= 8}

# 16. Get temperature in C and F
@app.get("/temp")
def temp(c: float):
    f = (c * 9/5) + 32
    return {"celsius": c, "fahrenheit": f}

# 17. Path + query: task with priority
@app.get("/task/{name}")
def task(name: str, priority: str):
    return {"task": name, "priority": priority}

# 18. Reverse text
@app.get("/reverse")
def reverse(text: str):
    return {"reversed": text[::-1]}

# 19. Multiply 2 numbers (path + query)
@app.get("/mul/{a}")
def mul(a: int, b: int):
    return {"result": a * b}

# 20. Check age eligibility
@app.get("/eligible")
def eligible(age: int):
    return {"eligible": age >= 18}

