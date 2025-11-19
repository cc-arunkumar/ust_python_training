from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

# 1. Greet user with optional name (query param default)
# @app.get("/greet")
# def greet(name: Optional[str] = "Guest"):
#     return {"message": f"Hello, {name}!"}

# # 2. Get square of a number (path param)
# @app.get("/square/{num}")
# def square(num: int):
#     return {"square": num * num}

# # 3. Check if number is even or odd (path)
# @app.get("/check/{num}")
# def check(num: int):
#     return {"result": "Even" if num % 2 == 0 else "Odd"}

# # 4. Simple addition using query params
# @app.get("/add")
# def add(a: int, b: int):
#     return {"sum": a + b}

# # 5. User info with optional city (path + optional query)
# @app.get("/user/{id}")
# def user_info(id: int, city: Optional[str] = None):
#     return {"id": id, "city": city if city else "Not Provided"}

# # 6. Repeat a message n times
# @app.get("/repeat")
# def repeat(msg: str, times: int):
#     return {"result": [msg for _ in range(times)]}

# # 7. Full name using two query parameters
# @app.get("/fullname")
# def fullname(first: str, last: str):
#     return {"fullname": f"{first} {last}"}

# # 8. Convert string to uppercase
# @app.get("/upper")
# def upper(text: str):
#     return {"uppercase": text.upper()}

# # 9. Calculate area of rectangle
# @app.get("/area")
# def area(length: int, width: int):
#     return {"area": length * width}

# # 10. Age next year
# @app.get("/age/{age}")
# def age_next(age: int):
#     return {"next_year_age": age + 1}

# # 11. Check if a word contains a character
# @app.get("/contains")
# def contains(word: str, char: str):
#     return {"contains": char in word}

# # 12. Combine path + multiple query params
# @app.get("/movie/{title}")
# def movie(title: str, year: int, rating: int):
#     return {"title": title, "year": year, "rating": rating}

# 13. Return list of numbers sent (query repeats)
@app.get("/nums")
def nums(n: List[int] = Query(...)):
    return {"numbers": n}

# # 14. Show substring of a string
# @app.get("/substring")
# def substring(text: str, start: int, end: int):
#     return {"substring": text[start:end]}

# # 15. Validate password length
# @app.get("/checkpass")
# def checkpass(pwd: str):
#     return {"valid": len(pwd) >= 8}

# # 16. Get temperature in C and F
# @app.get("/temp")
# def temp(c: float):
#     return {"Celsius": c, "Fahrenheit": (c * 9/5) + 32}

# # 17. Path + query: task with priority
# @app.get("/task/{taskname}")
# def task(taskname: str, priority: str):
#     return {"task": taskname, "priority": priority}

# # 18. Reverse text
# @app.get("/reverse")
# def reverse(text: str):
#     return {"reversed": text[::-1]}

# # 19. Multiply 2 numbers (path + query)
# @app.get("/mul/{a}")
# def multiply(a: int, b: int):
#     return {"product": a * b}

# # 20. Check age eligibility
# @app.get("/eligible")
# def eligible(age: int):
#     return {"eligible": age >= 18}
