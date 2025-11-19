# def main():
#     print("Hello from my-first-fastapi-app!")


# if __name__ == "__main__":
#     main()

from fastapi import FastAPI,Query

app=FastAPI()

# @app.get("/")
# def home():
#     return {"message":"Hello FastAPI + UV!"}


# @app.get("/greet/{name}")
# def greet(name:str):
#     return {"message":f"good afternoon, {name}"}

# @app.get("/add")
# def add(num1:int,num2:int,num3:int):
#     return {"sum":num1+num2}

# @app.get("/square/{num}") #path
# def square(num:int):
#     return {"square":num**2}

# @app.get("/square")
# def square(num:int=4):
#     return {"square":num**2}



# Task day 13
# 1.Greet user with optional name (query param default)
@app.get("/greet/{name}")
def greet(name:str):
    return {"name":f"{name}"}

# # output:
# http://127.0.0.1:8000/greet/name=rahul
# {"name":"name=rahul"}


#2.Get square of a number (path param)
@app.get("/square/{num}")
def square(num:int):
    return {"square":f"{num**2}"}

#output:
# http://127.0.0.1:8000/square/7
#{"square":"49"}


#Check if number is even or odd (path)
@app.get("/even_odd/{num}")
def even_odd(num:int):
    if num %2==0:
        return {"num":f"{num} is a even number"}
    else:
        return {"num":f"{num} is a odd number"}
    
# #output:
# http://127.0.0.1:8000/even_odd/12
# {"num":"12 is a even number"}
# http://127.0.0.1:8000/even_odd/15
# {"num":"15 is a odd number"}

#4.Simple addition using query params
@app.get("/add")
def add(num1:int,num2:int):
    return {"addition":f"{num1+num2}"}

#output:
# http://127.0.0.1:8000/add?num1=10&num2=15
#{"addition":"25"}

#5 User info with optional city (path + optional query)
@app.get("/user/{id}")
def user_info(id:int,city:str):
    return {"user info id":f"{id} city:{city}"}

# #output
# http://127.0.0.1:8000/user/24?city=mumbai
# {"user info id":"24 city:mumbai"}

#6..Repeat a message n times
@app.get("/repeat")
def repeat(msg:str,times:int):
    return {"repeated string":f"{msg*times}"}

#output
# http://127.0.0.1:8000/repeat?msg=hi&times=3
# {"repeated string":"hihihi"}

#7.Full name using two query parameters
@app.get("/fullname")
def fullname(first:str,last:str):
    return {"full name":f"{first+last}"}

#output
#http://127.0.0.1:8000/fullname?first=rahul&last=sharma
#{"full name":"rahulsharma"}

# 8.Convert string to uppercase
@app.get("/upper")
def upper(text:str):
    return {"upper case":f"{text.upper()}"}

#output
#http://127.0.0.1:8000/upper?text=hello
#{"upper case":"HELLO"}


#9.Calculate area of rectangle
@app.get("/area")
def area(length:int,width:int):
    return {"area of rectange":f"{length*width}"}

#output
# http://127.0.0.1:8000/area?length=5&width=3
# {"area of rectange":"15"}

# 10.Age next year
@app.get("/age/{num}")
def age(num:int):
    return {"next year":f"{num+1}"}

#output
# http://127.0.0.1:8000/age/24
# {"next year":"25"}

    
#11.Check if a word contains a character
@app.get("/contains")
def contains(word:str,char:str):
    if char in word:
        return {"char":f"{char} in word"}
    else:
        return {"char":f"{char} not found"}
    
#output:
# http://127.0.0.1:8000/contains?word=hello&char=l
# {"char":"l in word"}

#12.Combine path + multiple query params
@app.get("/movie/avatar")
def movie(year:int=2000,rating:int=9):
    return{"message":f"released in {year} and rating{rating}"}
#output:
# http://127.0.0.1:8000/movie/Avatar?year=2009&ratting=9
# {"movie":"year : 2009 ratting:9"}

# 13.Return list of numbers sent(query repeats)
@app.get("/nums")
def number(number:list[int]=Query()):
    list=[]
    for n in number:
        list.append(n)
    return {"List":list}
#output
# {
#   "List": [
#     10,
#     20,
#     30
#   ]
# }

#14.Show substring of a string
@app.get("/substring")
def sub(text:str="hello",start:int=0,end:int=3):
    return{"substring":text[start:end]}
#output
# {"substring":"ell"}

#15.Validate password length
@app.get("/checkpass")
def checking(pwd:str="abcd1234"):
    return{"length okay":len(pwd)>=8}

#output
# {"length okay":true}

#16.Get temperature in C and F
@app.get("/temp")
def temperature(c:int=10,f:int=82):
    return{"temperature":f"int c {c} in f{c+273}"}
#output
# {
#   "temperature": "int c 30 in f303"
# }


# 17.Path + query:task with priority
@app.get("/task/clean-room")
def cleanroom(priority:str="high"):
    return {"priority":priority}
#output
# {
#   "priority": "low"
# }

#18..Reverse text
@app.get("/reverse")
def reversing(text:str="hello"):
    return {"reversed string":text[::-1]}

#output
# {
#   "reversed string": "olleh"
# }

#19.Multiply 2 numbers (path + query)

@app.get("/mul/{num1}")
def multiply(num1:int,num2:int=1):
    return {"multiplyed":num1*num2}

#output
# {
#   "multiplyed": 72
# }

#20.Check age eligibility
@app.get("/eligible")
def validate(age:int=18):
    return{"valid":age>=18}

#output
# {
#   "valid": false
# }

    