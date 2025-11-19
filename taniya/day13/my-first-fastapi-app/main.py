# def main():
#     print("Hello from my-first-fastapi-app!")


# if __name__ == "__main__":
#     main()
from typing import List
from fastapi import FastAPI, Query
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello Fast API + UV! hiiiii hey"}

@app.get("/greet")
def greet(name:str ="taniya"):
    return {"message":f"Good Afternoon {name}"}

@app.get("/add")
def add(num1:int , num2:int,num3:int):
    return {"sum=":num1+num2+num3}  
 
@app.get("/sub")
def sub(num1:int,num2:int):
    return {"sub=":num1-num2} 
@app.get("/square/{num}")
def square(num:int):
    return {num*num}

@app.get("/square")
def square(num:int = 25):
    return{num*num}

@app.get("/number")
def check(num:int):
    return{"result":"even" if num%2==0 else "odd"}

@app.get("/user")
def user(id:int=24,city:str="Mumbai"):
    return{"id":id,"city":city}
    
@app.get("/repeat")
def repeat(msg:str,times:int):
    return{"result":" ".join([msg]*times)}

@app.get("/name")
def name(first_name:str,last_name:str):
    return{"first_name":f"{first_name} {last_name}"}

@app.get("/upper")
def upper(word:str):
    return{"uppercase":word.upper()}

@app.get("/area")
def area(length:int,width:int):
    return{"area":length*width}

@app.get("/age")
def age(age:int):
    return{"Age next year":age+1}

@app.get("/contains")
def contains(word:str,char:str):
    return{"result":char in word}

@app.get("/combine")
def combine(movie:str,year:int,rating:int):
    return{
        "movie":movie,
        "year":year,
        "rating":rating
    }

@app.get("/numss")
def numss(n:List[int] = Query(...)):
    return{"numbers":n}

@app.get("/substring")
def substring(text:str,first:int,last:int):
    return{"substring":text[first:last]}

@app.get("/password")
def password(pswd:str):
    if len(pswd)>=10:
        return{"valid":True}
    else:
        return{"valid":False,"reason":"password is valid"}

@app.get("/temp")
def temp(c:float):
    f = (c* 9/5) + 32
    return{"celsius":c,"fahrenheit":f}

@app.get("/task")
def task(task:str,priority:int):
    return{"task":task,"priority":priority}

@app.get("/reverse")
def reverse(word:str):
    return{"reverse word":word[::-1]}


@app.get("/mul")
def multiply(a: int, b: int):
    return {"result": a * b}

@app.get("/eligible")
def eligible(age: int):
    return {"eligible": age >= 18}
        
        


