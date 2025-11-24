from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

# Home endpoint
@app.get("/")
def home():
    return {"message": "Hyyyyyyy"}  # Basic greeting message

# 1. Greet endpoint - Takes a name as input and returns a greeting message
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"{name}"}  # Returns the name passed in the URL

# 4. Addition endpoint - Takes three integers as query parameters and returns their sum
@app.get("/add")
def add(a: int, b: int, c: int):
    return {"sum=": a + b + c}  # Returns the sum of a, b, and c

# 2. Square of a number - Takes a number and returns its square
@app.get("/square/{n}")
def square(n: int):
    return {"sq": n ** 2}  # Returns the square of the given number

# Default square endpoint - Uses a default value of 8 if no number is provided
@app.get("/square")
def square(n: int = 8):
    return {"sq": n ** 2}  # Returns the square of the number, default is 8

# 3. Check if number is even or odd
@app.get("/check")
def evenodd(n: int):
    if n % 2 == 0:
        return {"result": "Even"}  # Returns "Even" if the number is divisible by 2
    else:
        return {"result": "Odd"}  # Returns "Odd" if the number is not divisible by 2

# 8. Convert text to uppercase
@app.get("/upper")
def upper(text: str):
    return {"text": f"{text.upper()}"}  # Converts the input text to uppercase

# 7. Full name endpoint - Takes first and last name and returns them
@app.get("/fullname")
def name(first: str, last: str):
    return {"first": f"{first}", "last": f"{last}"}  # Returns the first and last name

# 9. Calculate area of a rectangle - Takes length and width as input
@app.get("/area")
def rectangle(length: int, width: int):
    return {"length": f"{length}", "width": f"{width}"}  # Returns the length and width of the rectangle

# 5. User details endpoint - Takes user id and city (default is Coimbatore)
@app.get("/user/{id}")
def user(id: int, city: str = "Coimbatore"):
    return {"user_id": id, "city": city}  # Returns the user ID and city

# 6. Repeat a message - Takes a message and a number to repeat it
@app.get("/repeat")
def repeat(msg: str, n: int):
    return {"message": msg * n}  # Repeats the message 'n' times

# 10. Age next year - Takes current age and returns age next year
@app.get("/age/{current_age}")
def age(current_age: int):
    return {"age_next_year": current_age + 1}  # Returns the age next year

# 11. Check if a character is in the word - Takes word and character as input
@app.get("/contains")
def contains(word: str, char: str):
    return {"contains": char in word}  # Checks if the character is present in the word

# 12. Movie details - Takes title, year (default 2009), and rating (default 9)
@app.get("/movie/{title}")
def movie(title: str, year: int = 2009, rating: int = 9):
    return {"title": title, "year": year, "rating": rating}  # Returns the movie details

# 13. List of numbers - Takes a list of integers
@app.get("/nums")
def nums(n: list[int]):
    return {"numbers": n}  # Returns the list of numbers

# 14. Get a substring - Takes text and start/end indices to return a substring
@app.get("/substring")
def substring(text: str, start: int, end: int):
    return {"substring": text[start:end]}  # Returns the substring based on start and end indices

# 15. Check password validity - Checks if password is at least 8 characters
@app.get("/checkpass")
def checkpass(pwd: str):
    return {"valid": len(pwd) >= 8}  # Returns whether the password length is valid (>= 8 characters)

# 16. Temperature conversion - Converts Celsius to Fahrenheit
@app.get("/temp")
def temp(c: float):
    return {"C": c, "F": (c * 9/5) + 32}  # Converts Celsius to Fahrenheit

# 17. Task details - Takes task name and priority (default is "low")
@app.get("/task/{name}")
def task(name: str, priority: str = "low"):
    return {"task": name, "priority": priority}  # Returns the task name and priority

# 18. Reverse a string - Takes a string and returns its reversed version
@app.get("/reverse")
def reverse(text: str):
    return {"reversed": text[::-1]}  # Returns the reversed string

# 19. Multiply two numbers - Takes two integers and returns their product
@app.get("/mul/{a}")
def mul(a: int, b: int):
    return {"product": a * b}  # Returns the product of 'a' and 'b'

# 20. Eligibility check - Takes age and returns whether the person is eligible (>=18)
@app.get("/eligible")
def eligible(age: int):
    return {"eligible": age >= 18}  # Returns whether the person is eligible (age >= 18)
