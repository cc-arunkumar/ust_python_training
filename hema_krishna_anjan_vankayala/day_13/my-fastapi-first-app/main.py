# def main():
#     print("Hello from my-fastapi-first-app!")


# if __name__ == "__main__":
#     main()

from fastapi import FastAPI , Query
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello Everyone!"}

#greet with specific name
@app.get("/greet")
def greet(name:str="Everyone"):
    return {"message":f"Hello {name}!"}

#sqaure by path parameters
@app.get("/square/{num}")
def sqaure(num:int): 
    return {"square": num**2}

#even or odd number 
@app.get("/check/{num}")
def check_even_odd(num:int):
    if num%2==0:
        return {"message":f"{num} is Even"}
    return {"message":f"{num} is Odd"}
#addition of 2 numbers
@app.get("/add")
def add(num1:int,num2:int):
    return {"sum":num1 + num2}

#user with city default Mumbai
@app.get("/user/{user_id}")
def user_info(user_id:int,city:str="Mumbai"):
    return {"user":f'Hello User {user_id} in {city}'}

#repeat message n times 
@app.get("/repeat")
def repeat_n(msg:str,times:int):
    return {"repeated_message":msg*times}

#full name using 2 queries
@app.get("/fullname")
def fullname(first:str,last:str):
    return {"fullanme": first+" "+last}

#uppercase of word
@app.get("/upper")
def upper_case(text:str):
    return {"upper":text.upper()}

#area of rectangle
@app.get("/area")
def area(length:int,width:int):
    return {"area": length*width}

#next year age 
@app.get("/age/{num}")
def age_next_year(num:int):
    return {"next_year_age":num+1}

#check word contains character 
@app.get("/contains")
def is_contains(word:str,char:str):
    return {"is_char_in_word": char in word}

#combine path multi queries
@app.get("/movie/{movie_name}")
def movie_rating(movie_name:str,year:int,rating:int):
    return {"movie_rating": f'Movie {movie_name} in Year {year} got Rating of {rating}'}

#return list of numbers sent
@app.get("/nums")
def list_nums(n:list[int]=Query()):
    return {"list_of_nums":n}

#show substring of string 
@app.get("/substring")
def substring(text:str,start:int,end:int):
    return {"substring":text[start:end]}

#validate password length 

@app.get("/checkpass")
def check_pass(pwd:str):
    return {"checkpass":len(pwd)>=8}

#get temperature from c to f 
@app.get("/temp")
def temp_to_f(c:int):
    return {"temp_f":c+273}

#task Priority 

@app.get("/task/{task_name}")
def task_prior(task_name:str,priority:str):
    return {"task":f"{task_name} is {priority} priority task"}

#reverse string 
@app.get("/reverse")
def reverse_string(text:str):
    return {"reverse":text[::-1]}

#multiply 2 numbers 
@app.get("/mul/{num1}")
def multiply(num1:int,num2:int):
    return {"multiply":num1*num2}

#check age eligiblity 

@app.get("/eligible")
def is_eligible(age:int):
    if age>=18:
        return {"is_eligible": "Eligible"}
    return {"is_eligible":"Not Eligible"}