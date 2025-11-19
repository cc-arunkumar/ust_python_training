from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI,This is My first"}

# query param
@app.get("/greet")
def greet(name:str="arun"):
    return {"message":f"Hi Good Afternoon {name}"}
        
#simple additon
@app.get("/add")
def add(num1:int,num2:int,num3:int):
    return {"sum:":num1+num2+num3}

# path query
@app.get("/square/{num}")

def square_num(num:int):
    return {"sqaure":f"{num*num}"}

#oddeven validation
@app.get("/evenodd/{num}")

def even_odd(num:int):
    if num%2==0:
        return {"message":f"{num} is even number"}
    else:
        return {"message":f"{num} is odd number"}

@app.get("/users/{age}")
@app.get("/users")
def user_info(age:int=24,city:str="Mumbai"):
    return {"message":f"users age:{age} and city:{city}"}



# repeat a message n times
@app.get("/repeat")
def repeat(mssg:str="hi",times:int=3):
    return {"message":f"{mssg*times}"}

# full name 
@app.get("/fullname")
def fullname(first:str="rahul",last:str="sharma"):
    return {"message":f"firstName:{first} LastName:{last}"}

# Convert string to Uppercase
@app.get("/upper")
def convertupper(text:str="hello"):
    return {"message":f"ToUppercase {text.upper()}"}
    

# calculate area of rectangle
@app.get("/area")
def getarea(length:int=5,breadth:int=3):
    return {"message":f"Area of rectangle:{length*breadth}"}

# age next year
@app.get("/age/{year}")
def next_year(year:int):
    return {"message":f"next year:{year+1}"}

#word contains a charcetr
@app.get("/conatins")
def char_in_str(word:str,char:str):
    if char in word:
        return {"message":f"{char} is in {word}"}
    else:
        return {"message":f"{char} not in {word}"}
    
    
# combine path and mutliple queries
@app.get("/movie/{name}")
def get_movie(name:str,year:int=2000,rating:int=9):
    return {"message":f"name:{name} year:{year} rating:{rating}"}


# return list os numbers
from fastapi import Query
@app.get("/nums")
def get_nums(num1:list[int]=Query(...)):
    return {"message":f"numbers:{num1}"}


#sho substring of strng
@app.get("/substring")
def get_substring(text:str,start:int,end:int):
    return {"message":f"{text[start:end]}"}

#validate password

@app.get("/checkpass")
def validate(psswd:str):
    if psswd.isalnum() and len(psswd)==6:
        return {"message":f"{psswd} is valid"}
    else:
        return {"message":f"{psswd} is invalid"}
    
# get temperature in c and f
@app.get("/temp/{c}")
def temperature(c:int):
    return {"message":f"celsius {c}"}

#task with priority
@app.get("/task/{room}")

def check(room:str,priority:str="high"):
    return {"message": f" {room } with {priority} priority"}

#reverse text
@app.get("/reverse")
def reverse(text:str):
    return {"message":f"{text[::-1]}"}

#mutliply 2 numbers
@app.get("/mul/{num}")
def multiply(num:int,num2:int=9):
    return {"message":f"mulres:{num*num2}"}

@app.get("/eligible")
def eligibility(age:int):
    if age>=18:
        return {"message":f"{age} is eligible"}
    else:
        return {"message":f"{age} is not eleigible"}
    
    
    














# query
# /path?nums=val&num2=Value 
# path->single
# /path/val