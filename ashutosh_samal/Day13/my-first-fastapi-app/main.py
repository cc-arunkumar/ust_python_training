
from fastapi import FastAPI
app = FastAPI()

# @app.get("/")
# def home():
#     return {"message":"Hello FastAPI + UV!"}

# @app.get("/greet")
# def greet(name:str="User"):
#     return {"message":f"Hello {name}"}

# @app.get("/add")
# def add(num1:int,num2:int,num3:int):
#     return{"sum =":num1+num2+num3}

# @app.get("/square1/{num1}")
# def square(num1:int):
#     return {"square = ":num1*num1}

# @app.get("/square2")
# def square(num1:int):
#     return {"square = ":num1*num1}

# @app.get("/square3")
# def square(num1: int = 2):  # Default value is 2
#     return {"square": num1 * num1}


# 1. Greet user with an optional name (query param default)
@app.get("/greet")
def greet(name:str="User"):
    return {"message":f"Hello {name}"}

# 2. Return the square of a number from the path
@app.get("/square/{num}")
def square(num:int):
    return{"Square ":num*num}

# 3. Check if a number is even or odd
@app.get("/check/{num}")
def check(num:int):
    if num % 2 == 0:
        return {f"{num} is even"}
    else:
        return {f"{num} is odd"}

# 4. Add two numbers and return the sum
@app.get("/add")
def add(num1:int, num2:int):
    return {"sum =": num1 + num2}

# 5. Return user details with optional city as query parameter
@app.get("/user/{u_id}")
def user(u_id:int, city:str="N/A"):
    return {"User ID": u_id, "City": city}

# 6. Repeat a message a specified number of times
@app.get("/repeat")
def repeat(msg:str, times:int):
    return msg * times

# 7. Return the full name by combining first and last name
@app.get("/fullname")
def fullname(first:str, last:str):
    return {"Full Name ": first + last}

# 8. Convert the given text to uppercase
@app.get("/upper")
def upper(text:str):
    return text.upper()

# 9. Calculate the area of a rectangle from length and width
@app.get("/area")
def area(length:int, width:int):
    return {"Area Rectangle": length * width}

# 10. Calculate the age of the person next year
@app.get("/age/{age}")
def age(age:int):
    return {"Age next year =": age + 1}

# 11. Check if a character is present in the word
@app.get("/contains")
def contains(word:str, char:str):
    if char in word:
        return {f"{word} contains {char}"}

# 12. Return details of a movie: name, year, and rating
@app.get("/movie/{name}")
def movie(name:str, year:int, rating:int):
    return {f"Name of Movie:{name}  Year:{year}  Rating:{rating}"}

# 13. Return a list of three numbers
@app.get("/nums")
def nums(n1:int, n2:int, n3:int):
    l1 = []
    l1.append(n1)
    l1.append(n2)
    l1.append(n3)
    return {"List of Numbers": l1}

# 14. Return a substring from the given text
@app.get("/substring")
def substring(text:str, start:int, end:int):
    return text[start:end]

# 15. Check if the password is valid (at least 8 characters)
@app.get("/checkpass")
def checkpass(pwd:str):
    if len(pwd) >= 8:
        return {"password is valid"}

# 16. Convert Celsius to Fahrenheit
@app.get("/temp")
def temp(c:int):
    return {f"F = {(c * 9 / 5) + 32}"}

# 17. Return task with its priority
@app.get("/task/{task}")
def task(task:str, priority:str):
    return {f"{task} has priority {priority}"}

# 18. Reverse the given text
@app.get("/reverse")
def reverse(text:str):
    return text[::-1]

# 19. Multiply two numbers and return the product
@app.get("/mul/{a}")
def mul(a:int, b:int):
    return {f"Product is: {a * b}"}

# 20. Check if the person is eligible (age >= 18)
@app.get("/eligible")
def eligible(age:int):
    if age >= 18:
        return {f"{age} is valid age"}

    
    
#Sample Output
# {"message":"Hello Ashutosh"}
# {"Square ":25}
# ["12 is even"]
# {"sum =":5}
# {"User ID":24,"City":"Mumbai"}
# "hellohellohello"
# {"Full Name ":"AshutoshSamal"}
# "HELLO"
# {"Area Rectangle":6}
# {"Age next year =":19}
# ["hello contains o"]
# ["Name of Movie:Avatar  Year:2009  Rating:9"]
# {"List of Numbers":[2,3,4]}
# "ell"
# ["password is ok"]
# ["F =86.0"]
# ["cleanroom has priority high"]
# "olleh"
# ["Product is:50"]
# ["18 is valid age"]
