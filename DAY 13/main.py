# def main():
#     print("Hello from my-first-fastapi-app!")


# if __name__ == "__main__":
#     main()

from fastapi import FastAPI

app=FastAPI()

# @app.get("/")
# def home():
#     return {"message": "HI, Im gowtham"}

# @app.get("/greet/{name}")
# def greet(name:str):
#     return {"message":f"HI {name}"}

# @app.get("/add")
# def add(num1:int, num2:int,num3:int):
#     return {"sum=":num1+num2+num3}

# @app.get("/square")
# def square(num:int=10):
#     return {f"Square is {num*num}"}

# @app.get("/square")
# def square(num:int):
#     return {f"Square is {num*num}"}



# -----------------------------------------

@app.get("/greet/{name}")
def greet(name:str):
    return f"Hello {name}, Good Morning"

@app.get("/greet")
def greet(name:str="Gowtham"):
    return f"Hello {name}"

@app.get("/square/{num}")
def square(num:int):
    return f"Sqiare of {num} is {num*num}"

@app.get("/check/{num}")
def check(num:int):
    if num%2==0:
        return f"{num} is Even Number"
    else : return f"{num} is Odd NUmber"

@app.get("/add")
def add(a:int,b:int):
    return f"Addition is {a+b}"

@app.get("/user/{id}")
def user(id:int,city=None):
    return {"id" :id, "city" : city}
# http://127.0.0.1:8000/user/10?city=kochi

@app.get("/repeat")
def repeat(msg:str,time:int):
    return {"Repeat ": msg*time}
# http://127.0.0.1:8000/repeat?msg=hi&time=10

@app.get("/fullname")
def fullname(first:str,last:str):
    return {"Full name": first + last}

@app.get("/upper")
def upper(text:str):
    return {"upper":text.upper()}
# http://127.0.0.1:8000/upper?text=hi

@app.get("/area")
def area(length:int,width:int):
    return {"Area of Rectangle is ":length*width}
# http://127.0.0.1:8000/area?length=10&width=20

@app.get("/age/{my_age}")
def age(my_age:int):
    return {"Next Age ":my_age+1}
# http://127.0.0.1:8000/age/19

@app.get("/contains")
def contains(word:str, char:str):
    return {"contains": char in word}
# http://127.0.0.1:8000/contains?word=Gowtham&char=a

@app.get("/movie/{title}")
def movie(title: str,year:int,rating:float):
    return {"Movie name" :title , "year": year , "rating": rating}
# http://127.0.0.1:8000/movie/beast?year=2023&rating=8.1

@app.get("/nums")
def nums(n:list[int]):
    return {"Numbers":n}

@app.get("/substring")
def substring(text:str, start:int, end:int):
    return {"Substring":text[start:end]}
# http://127.0.0.1:8000/substring?text=helloworld&start=0&end=5

@app.get("/checkpass")
def checkpass(pwd:str):
    valid=len(pwd)>=8
    return {"Valid":valid}
# http://127.0.0.1:8000/checkpass?pwd=Gowtham1234


@app.get("/temp")
def temp(c :float):
    f=(c* 9/5)+32
    return {"Celsius":c,"Fahrenheit":f}
# http://127.0.0.1:8000/temp?c=30

@app.get("/task/{name}")
def task(name:str,priority:str):
    return {"Task name":name, "Priority":priority}
# http://127.0.0.1:8000/task/clean-room?priority=high

@app.get("/reverse")
def reverse(text:str):
    return {"Reversed": text[::-1]}
# http://127.0.0.1:8000/reverse?text=Gowtham

@app.get("/mul/{a}")
def mul(a:int,b:int):
    return {"Result":a*b}
# http://127.0.0.1:8000/mul/4?b=2

@app.get("/eligible")
def eligible(age:int):
    return {"Eligible ":age>=18}

# http://127.0.0.1:8000/eligible?age=80