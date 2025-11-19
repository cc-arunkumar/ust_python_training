from fastapi import FastAPI,Query
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello Fastapi bye Fastapi + UV!"}

@app.get("/greet")
def greet(name:str):
    return {"greet message":f"Hi {name} good afternoon"} #Output: {"greet message":"Hi Akhil good afternoon"

@app.get("/square/{num}")
def square(num:int): 
    return {"square " : f"{num**2}"} #output: {"square ":"9"}

@app.get("/add")
def add(a:int,b:int): 
    return {"sum = " : a + b} #output: {"sum = ":3}

@app.get("/user/{id}")
def user(id:int,city:str = "kerala"): #output: {"id":24,"City":"kerala"}
    return {"id" : id,"City":city}

@app.get("/repeat")
def repeat(msg:str,times:int):  #Output: "akhilakhilakhil"
    return msg*times

@app.get("/fullname")
def fullname(first:str,last:str):
    return {"Full name":first+" "+last}

@app.get("/upper")
def upper(string:str):
    return {string:string.upper()}

@app.get("/area")
def area(length:int,width:int):
    return {"Area":length*width}

@app.get("/age/{age}")
def age(age:int):
    return {"Next year age":age+1}

@app.get("/contains")
def contains(word:str,char:str):
    return {"Contains": True if char in word else False}

@app.get("/movie/{name}")
def movie(name:str,year:int,rating:int):
    return {"Movie Name":name,"Year":year,"Rating":rating}

@app.get("/num")
def num(n:list[int]=Query(...)):    #output: {n:[1,2,3]}
    return {"n":n}

@app.get("/substring")
def substring(text:str,start:int,end:int):
    return {"Substring":text[start:end]}

@app.get("/checkpass")
def checkpass(password:str):
    return {"CheckPass":True if len(password)==8 else False}

@app.get("/temp")
def temp(c:int):
    return {"C":c,"F":c*(9/5)+32}

@app.get("/task/name")
def task(name:str,priority:str):
    return {"Task":name,"Priority":priority}

@app.get("/reverse")
def reverse(text:str):
    return {"Reverse": text[::-1]}

@app.get("/multiply/{a}")
def multiply(a:int,b:int):
    return {"mult": a*b}

@app.get("/eligible")
def eligible(aage:int):
    return {"Age": age,"Valid":True if age>=18 else False}
