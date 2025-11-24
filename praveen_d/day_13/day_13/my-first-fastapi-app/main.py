# def main():
#     print("Hello from my-first-fastapi-app!")


# if __name__ == "__main__":
#     main()

from fastapi import FastAPI, Query
from typing import List
app = FastAPI()


@app.get("/")
def hello():
    return {"message" : "Hello Praveen from praveen !"}

# 1.Greet user with optional name (query param
# default)
# URL examples:
# /greet
# /greet?name=rahul
@app.get("/greet/{name}")
def greet(name:str):
    return{"msg":f"GB{name}"}




# 2.Get square of a number (path param)
# URL: /square/7
@app.get("/square/{num1}")
def add(num1:int):
    return{ "square":num1*num1}

# 3.Check if number is even or odd (path)
# /check/12
@app.get("/evenorodd/{value}")
def classify(value:int):
    if value%2==0:
        return{"Even":"even"}
    else:
        return {"Odd":"odd"}

# 4.Simple addition using query params
# /add?a=10&b=5
@app.get("/add")
def add(num1:int,num2:int):
    return{ "sum":num1+num2}

# 5.User info with optional city (path)
# /user/24
@app.get("/user/{user_id}")
def user(user_id:int):
    if user_id==24:
        return """David
                Chennai,
                121212121212
    """
    else:
        return "No-results found"
    
print("**************************************************************")
# 5.User info with optional city (optional query)    
# /user/24?city=Mumbai
@app.get("/user/{user_id}")
def userr(user_id:int,city:None):
    if user_id==24:
        response={
            "name":"David",
            "location": city if city else "mumbai",
            "number":121212121212
            }
        return response
           
    else:
        return "No records found"
print("**************************************************************")
        
# 6.Repeat a message n times
# /repeat?msg=hi&times=3
@app.get("/repeat")
def repeat(msg:str,times:int):
    list=[]
    for i in range(0,times):
        list.append(msg)
    return list

# 7.Full name using two query parameters
# /fullname?first=rahul&last=sharma
@app.get("/fullname")
def repeat(name1:str,name2:str):
    name=name1+name2
    return name

# 8.Convert string to uppercase
# /upper?text=hello
@app.get("/upper")
def repeat(input_string:str):
    return input_string.upper()

# 9.Calculate area of rectangle
# /area?length=5&width=3
@app.get("/area")
def area(length:int,width:int):
    return {"area":length*width}

# 10.Age next year
# /age/24
@app.get("/age/{age}")
def age(age:int):
    return {"area":age+1}

# 11.Check if a word contains a character
# /contains?word=hello&char=l
@app.get("/contains")
def age(word:str,char:str):
    if char in word:
        return "contains"
    else:
        return "Not contains"
    
# 12.Combine path +
@app.get("/movie")
def age(movie:str="Avatar",year:int=2009,rating:int=7):
    return {movie,year,rating}

#  12.multiple query params
# /movie/Avatar?year=2009&rating=7
@app.get("/movie/Avatar")
def age(year:int,rating:int):
    return {"Avatar",year,rating}

# 13.Return list of numbers sent(query repeats)
# /nums?n=1&n=2&n=3
@app.get("/nums")
def get_numbers(n: List[int]=Query(...)):
    return {"numbers": n}


# 14.Show substring of a string
# /substring?text=hello&start=1&end=4
@app.get("/substring")
def substring(text:str,start:int,end:int):
    new_string=text[start:end]
    return {"str:",new_string}

# 15.Validate password length
# /checkpass?pwd=abcd1234
@app.get("/checkpass")
def substring(pwd:str):
    if len(pwd)>8 and len(pwd)<12:
        return {"valid:",True}
    else:
        return {False}
    
# 16.Gettemperature in C and F
# /temp?c=30
@app.get("/temp")
def temp(c:int):
    fahrenheit = (9/5) * c + 32
    return fahrenheit
    
# 17.Path + query:task with priority
# /task/clean-room?priority=high
@app.get("/task/clean/{priority}")
def temp(priority:str):
    if priority=="high":
        return {"Immideate action required"}
    elif priority=="medium":
        return {"action required"}
    else :
        return {"Clean as soon as possible"}
    
# 18.Reverse text
# /reverse?text=hello
@app.get("/reverse/{text}")
def temp(text:str):
    new_text=text[::-1]
    return {new_text}

# 19.Multiply 2 numbers (path + query)
# /mul/10?b=5

@app.get("/mul")
def mul(num1:int,num2:int):
    return{ "Multiplication":num1*num2}

# 20.Check age eligibility
# /eligible?age=17
@app.get("/eligible")
def eligible(age:int):
    if age>=18:
        return {"Eligible"}
    else:
        return {"not Eligible"}

    