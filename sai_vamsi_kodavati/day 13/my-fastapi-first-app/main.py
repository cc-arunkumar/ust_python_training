from fastapi import FastAPI

app = FastAPI()

# 1.Greet user with optional name (query param default)

@app.get("/")
def home():
    return {"message":"Python FastAPI Training session"}
 
@app.get("/greet/{name}")   
def greet(name:str):
    return {"message":f"Good Morning {name}"}


# 2.Get square of a number (path param)
@app.get("/square")
def square(num:int = 5):
    return {"square":num*num}

# 3.Check if number is even or odd (path)
@app.get("/even/{num}")
def even(num:int):
    if num%2==0:
        return {"Even":num}
    else:
        return {"odd":num}
   

# 4.Simple addition using query params
@app.get("/add")
def add(num1:int,num2:int,num3:int):
    return {"sum":num1 + num2 + num3}

# 5.User info with optional city (path + optional query)
@app.get("/city/{num}")
def city(num:int,name:str = "Trivandrum"):
    return {f"num":{num},"City":{name}}

# 6.Repeat a message n times
@app.get("/repeat")
def repeat(msg:str,times:int):
    return {f"Msg n times":{msg*times}}

# 7.Full name using two query parameters
@app.get("/fullname")
def fullname(first:str,last:str):
    return {f"fullname":f"{first}{last}"}

# 8.Convert string to uppercase
@app.get("/uppercase")
def uppercase(text:str):
    case = text.upper()
    return {f"Uppercase of text:":{case}}

# 9.Calculate area of rectangle
@app.get("/area")
def area(l:int,b:int):
    return {f"Area of rectangle:":{l*b}}


# 10.Age next year
@app.get("/next_age/{age}")
def next_age(age:int):
    return {f"age next year:":{age+1}}


# 11.Check if a word contains a character
@app.get("/word")
def contains(word:str,char:str):
    for i in word:
        if i== char:
            return ("Character present in word")
        else:
            return ("Char not present")
    

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


# --------------------------------------------------------------------------------------

# Sample Output
# 1. Greet user with optional name (query param default)

# Request:

# GET /

# Response:

# {
#   "message": "Python FastAPI Training session"
# }

# Request:

# GET /greet/John

# Response:

# {
#   "message": "Good Morning John"
# }

# 2. Get square of a number (path param)

# Request:

# GET /square?num=4

# Response:

# {
#   "square": 16
# }

# 3. Check if number is even or odd (path)

# Request:

# GET /even/10

# Response:

# {
#   "Even": 10
# }
# Request:

# GET /even/7

# Response:

# {
#   "odd": 7
# }

# 4. Simple addition using query params

# Request:

# GET /add?num1=2&num2=3&num3=4

# Response:

# {
#   "sum": 9
# }

# 5. User info with optional city (path + optional query)

# Request:

# GET /city/1?name=New York

# Response:

# {
#   "num": 1,
#   "City": "New York"
# }

# Request:

# GET /city/2

# Response:

# {
#   "num": 2,
#   "City": "Trivandrum"
# }

# 6. Repeat a message n times

# Request:

# GET /repeat?msg=Hello&times=3

# Response:

# {
#   "Msg n times": "HelloHelloHello"
# }
# 7. Full name using two query parameters

# Request:

# GET /fullname?first=John&last=Doe

# Response:

# {
#   "fullname": "JohnDoe"
# }

# 8. Convert string to uppercase

# Request:

# GET /uppercase?text=hello

# Response:

# {
#   "Uppercase of text:": "HELLO"
# }

# 9. Calculate area of rectangle

# Request:

# GET /area?l=5&b=4

# Response:

# {
#   "Area of rectangle:": 20
# }

# 10. Age next year

# Request:

# GET /next_age/25

# Response:

# {
#   "age next year:": 26
# }

# Request:
    
# GET /eligible?age=17
# Response:
# {
#   "eligible": false
# }
