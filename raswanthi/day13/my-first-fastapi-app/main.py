from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "helloooo"}

# 1. Greet user (path param)
@app.get("/greet/{name}")
def greet(name:str):
    return {"message": f"welcome {name}"}

# 4. Addition (query params)
@app.get("/add")
def add(a:int,b:int):
    return {"sum": a + b}

# 2. Square (path param)
@app.get("/square/{num}")
def square(num:int):
    return {"square": num * num}

# 3. Even or odd (path param)
@app.get("/check/{num}")
def check(num:int):
    return {"result": "even" if num % 2 == 0 else "odd"}

# 5. User info (path + optional query)
@app.get("/user/{id}")
def user(id:int, city:str="Coimbatore"):
    return {"user_id": id, "city": city}

# 6. Repeat message (query params)
@app.get("/repeat")
def repeat(msg:str,n:int):
    return {"message": msg * n}

# 7. Full name (query params)
@app.get("/fullname")
def fullname(first:str,last:str):
    return {"full_name": f"{first} {last}"}

# 8. Uppercase string
@app.get("/upper")
def uppercase(text:str):
    return {"upper_case": text.upper()}

# 9. Rectangle area
@app.get("/area")
def area(length:int, width:int):
    return {"area": length * width}

# 10. Age next year (path param)
@app.get("/age/{current_age}")
def age(current_age:int):
    return {"age_next_year": current_age + 1}

# 11. Contains character
@app.get("/contains")
def contains(word:str,char:str):
    return {"contains": char in word}

# 12. Movie info (path + query)
@app.get("/movie/{title}")
def movie(title:str,year:int=2009,rating:int=9):
    return {"title": title, "year": year, "rating": rating}

# 13. List of numbers (query repeats)
@app.get("/nums")
def nums(n: list[int]):
    return {"numbers": n}

# 14. Substring
@app.get("/substring")
def substring(text:str,start:int,end:int):
    return {"substring": text[start:end]}

# 15. Validate password length
@app.get("/checkpass")
def checkpass(pwd:str):
    return {"valid": len(pwd) >= 8}

# 16. Temperature in C and F
@app.get("/temp")
def temp(c:float):
    return {"C": c, "F": (c * 9/5) + 32}

# 17. Task with priority
@app.get("/task/{name}")
def task(name:str,priority:str="low"):
    return {"task": name, "priority": priority}

# 18. Reverse text
@app.get("/reverse")
def reverse(text:str):
    return {"reversed": text[::-1]}

# 19. Multiply numbers (path + query)
@app.get("/mul/{a}")
def mul(a:int,b:int):
    return {"product": a * b}

# 20. Age eligibility
@app.get("/eligible")
def eligible(age:int):
    return {"eligible": age >= 18}

    
        
    


    

