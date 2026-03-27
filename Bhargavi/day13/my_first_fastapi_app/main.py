# GET Tasks
# 1.Greet user with optional name (query param
# default)
# URL examples:
# /greet
# /greet?name=rahul
# 2.Get square of a number (path param)
# URL: /square/7
# 3.Check if number is even or odd (path)
# /check/12
# 4.Simple addition using query params
# /add?a=10&b=5
# 5.User info with optional city (path + optional query)
# /user/24
# /user/24?city=Mumbai
# 6.Repeat a message n times
# /repeat?msg=hi&times=3
# 7.Full name using two query parameters
# /fullname?first=rahul&last=sharma
# 8.Convert string to uppercase
# GET Tasks 1
# /upper?text=hello
# 9.Calculate area of rectangle
# /area?length=5&width=3
# 10.Age next year
# /age/24
# 11.Check if a word contains a character
# /contains?word=hello&char=l
# 12.Combine path + multiple query params
# /movie/Avatar?year=2009&rating=9
# 13.Return list of numbers sent(query repeats)
# /nums?n=1&n=2&n=3
# 14.Show substring of a string
# /substring?text=hello&start=1&end=4
# 15.Validate password length
# /checkpass?pwd=abcd1234
# 16.Gettemperature in C and F
# /temp?c=30
# 17.Path + query:task with priority
# /task/clean-room?priority=high
# 18.Reverse text
# GET Tasks 2
# /reverse?text=hello
# 19.Multiply 2 numbers (path + query)
# /mul/10?b=5
# 20.Check age eligibility
# /eligible?age=17
# GET Tasks 3
from fastapi import FastAPI
app = FastAPI()

# @app.get("/greet/{name}")
# def greet(name: str):
#     return {"message": f"good bye {name}"}


# @app.get("/add")
# def add(num1:int,num2:int,num3:int):
#     return {"sum =":num1 +num2+num3}

# @app.get("/sub")
# def sub(num1:int,num2:int):
#     return{"sub =" :num1-num2}

# @app.get("/square/{num}")
# def square(num:int):
#     return{"square =" : num ** 2}

# @app.get("/square")
# def square(num:int):
#     return{"square =" : num ** 2}

# # def main():
# #     print("Hello from my-first-fast-app!")


# # if __name__ == "__main__":
# #     main()
# from fastapi import FastAPI
# app=FastAPI()

# @app.get("/")
# def home():
#     return {"message":"Hello hiiii FastApi+UV!"}

# @app.get("/greet/{name}")
# def greetings(name:str):
#     return{"message":f"Greetings from ust {name} "}

# @app.get("/add")
# def add(num1:int,num2:int):
#     return {"sum":num1+num2}

# @app.get("/square/{num}")
# def square(num:int):
#     return {"message":num*num} 

# @app.get("/square")
# def square(num:int):
#     return {"message":num*num}

from fastapi import FastAPI,Query
app=FastAPI()

@app.get("/")
def home():
    return {"message": "Hello hiiii FastApi+UV!"}

@app.get("/greet")
def greeting(name:str="Guest"):
    return {"message":f"Greetings from Ust {name} "}

@app.get("/square/{num}")
def square(num:int):
    return {"Square of number":num}
#{
#   "Square of number": 7
# }

@app.get("/check/{num}")
def checking(num:int):
    if num%2==0:
        message="even"
    else:
        message="odd"
    return{"The given number is":message}
# {
#   "The given number is": "odd"
# }

@app.get("/add")
def add(num1:int=1,num2:int=1):
    return {"the addition of two numbers is":num1+num2}
# {
#   "the addition of two numbers is": 11
# }

@app.get("/user/{id}")
def userdetails(id:int,city:str="karnataka"):
    return {"the user details are":f"{id} and {city}"}
# {
#   "the user details are": "24 and karnataka"
# }

@app.get("/repeat")
def repetation(msg:str="hi",times:int=1):
    return {"message":msg*times}
# {
#   "message": "hihihi"
# }

@app.get("/fullname")
def fullname(first:str="Bhargavi",last:str="settipalli"):
    return {"full name":f"{first},{last}"}
# {
#   "full name": "Bhargavi,settipalli"
# }

@app.get("/upper")
def uppercase(text:str="hello"):
    return {"upper case converted":text.upper()}
# {
#   "upper case converted": "BHARGAVI"
# }


@app.get("/area")
def area(length:int=1,width:int=2):
    return {"area":length*width}
# {
#   "area": 200
# }

@app.get("/age")
def age(age:int=16):
    return{"next year":age+1}
# {
#   "next year": 17
# }

@app.get("/contains")
def conatins(word:str="hello",ch:str="l"):
    return{"character in string":ch in word}
# {
#   "character in string": true
# }

@app.get("/movie/avatar")
def movie(year:int=2000,rating:int=9):
    return{"message":f"released in {year} and rating{rating}"}
# {
#   "message": "released in 2007 and rating8"
# }

@app.get("/nums")
def number(number:list[int]=Query()):
    list=[]
    for n in number:
        list.append(n)
    return {"List":list}
# {
#   "List": [
#     10,
#     20,
#     30
#   ]
# }

@app.get("/substring")
def sub(text:str="hello",start:int=0,end:int=3):
    return{"substring":text[start:end]}
# {
#   "substring": " sun"
# }

@app.get("/checkpass")
def checking(pwd:str="abcd1234"):
    return{"length okay":len(pwd)>=8}
# {
#   "length okay": true
# }

@app.get("/temp")
def temperature(c:int=10,f:int=82):
    return{"temperature":f"int c {c} in f{c+273}"}
# {
#   "temperature": "int c 30 in f303"
# }

@app.get("/task/clean-room")
def cleanroom(priority:str="high"):
    return {"priority":priority}
# {
#   "priority": "low"
# }

@app.get("/reverse")
def reversing(text:str="hello"):
    return {"reversed string":text[::-1]}
# {
#   "reversed string": "olleh"
# }

@app.get("/mul/{num1}")
def multiply(num1:int,num2:int=1):
    return {"multiplyed":num1*num2}
# {
#   "multiplyed": 72
# }

@app.get("/eligible")
def validate(age:int=18):
    return{"valid":age>=18}
# {
#   "valid": false
# }

    