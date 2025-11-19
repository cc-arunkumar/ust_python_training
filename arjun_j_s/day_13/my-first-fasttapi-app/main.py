from fastapi import FastAPI,Query



app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Welcome to FastAPI"}

@app.get("/greet/{name}")
def greet(name:str):
    return {"message" : f"Hiiii Sugavano {name}!!!"}

@app.get("/add")
def add(a:int,b:int,c:int):
    return {"Sum is" : f"{a+b+c}"}

@app.get("/square/{number}")
def square(number:int):
    return {"Square is" : f"{number**2}"}

@app.get("/square")
def square(number:int):
    return {"Square is" : f"{number**2}"}


@app.get("/check/{num}")
def check(num:int):
    if(num%2==0):
        return {num : "is even"}
    else:
        return {num : "is odd"}
    
@app.get("/user/{id}")
def user(id:int,city:str="Mumbai"):
    return {id: city}

@app.get("/repeat")
def repeat(msg:str,times:int):
    return {"message" : msg*times}


@app.get("/fullname")
def repeat(first:str,last:str):
    return {"message" : first+" "+last}

@app.get("/upper")
def upper(text:str):
    return {"output":text.upper()}

@app.get("/area")
def area(length:int,breadth:int):
    return {"area":length*breadth}

@app.get("/age/{age}")
def age(age:int):
    return {"Next Year you will be":age+1}

@app.get("/contains")
def contains(word:str,char:str):
    if(char in word):
        return {"message" : "Yes Found"}
    else:
        return {"message" : "Not Found"}
    
@app.get("/movie/{movie}")
def movie(movie:str,year:int,rating:int):
    return {"output":f"{movie} was released in {year} with a rating of {rating}"}

@app.get("/nums")
def nums(n:list[int]=Query(...)):
    return {"output" : n}

@app.get("/substring")
def substring(text:str,start:int,end:int):
    return {"output":text[start:end+1]}

@app.get("/checkpass")
def checkpass(pwd:str):
    return {"output": True if len(pwd.strip())!=0 else False}

@app.get("/temp")
def temp(c:int):
    return {"Temperature in F":(c*9/5) +32}

@app.get("/task/{task}")
def task(task:str,priority:str):
    return { "Output" : f"{task} has a {priority} priority"}

@app.get("/reverse/{text}")
def reverse(text:str):
    return {"Reverse":text[::-1]}

@app.get("/multiply/{num1}")
def multiply(num1:int,num2:int):
    return {"product": num1*num2}

@app.get("/eligible/{age}")
def eligible(age:int):
    return {"eligible": True if age>=18 else False}






