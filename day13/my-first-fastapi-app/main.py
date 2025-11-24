# Task on get method


# 1. Home Route (/): A simple home route that returns a message saying "fast api demo".
# 2. Greet User (/greet/{name}): Takes a name as a path parameter and returns a greeting message.
# 3. Addition (/add): Adds three query parameters (num1, num2, num3) and returns their sum.
# 4. Square (/square or /square/{num}): Computes the square of a number. Defaults to 9 if no number is passed.
# 5. Even/Odd (/evenodd/{num}): Checks if a number is even or odd.
# 6. User Info (/users): Takes age and city as query parameters and returns a message with this information.
# 7. Repeat Message (/repeat): Repeats a given message a certain number of times.
# 8. Full Name (/fullname): Combines first and last names into a full name.
# 9. Uppercase (/uppercase): Converts a given string to uppercase.
# 10. Area of Triangle (/area_of_triangle): Calculates the area of a triangle using length and breadth.
# 11. Age Next Year (/age_next_year): Calculates the user's age next year.
# 12. Character in Word (/char_contains_in_word): Checks if a character exists in a word.
# 13. Movie Info (/movie/{name}): Displays a movie's name, year, and rating.
# 14. List of Numbers (/nums): Accepts a list of numbers and returns them.
# 15. Substring (/substring_of_a_string): Returns a substring of a given string.
# 16. Password Validation (/validate): Checks if a password is alphanumeric and exactly 10 characters long.
# 17. Temperature (/temperature/{celcius}): Returns the Celsius value.
# 18. Task Priority (/task/{room}): Displays room details with an optional priority parameter.
# 19. Reverse Text (/reverse): Reverses a given string.
# 20. Multiply (/mul/{num}): Multiplies two numbers, with a default second number of 9.
# 21. Age Eligibility (/eligible): Checks if the age is 18 or older.




from fastapi import FastAPI

# Initialize FastAPI application
app = FastAPI()

# Basic route - Home route
@app.get("/")
def home():
    return {"message": "fast api demo"}  # Returns a simple message when accessed

# Greet user with a dynamic name in the URL path
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Good morning, {name}"}  # Returns a greeting message with the name provided in the URL

# Addition of three numbers, using query parameters
@app.get("/add")
def add(num1: int, num2: int, num3: int):
    return {"sum": num1 + num2 + num3}  # Returns the sum of the three numbers passed in the query

# Calculate the square of a number, with a default value of 9
@app.get("/square")
@app.get("/square/{num}")
def square(num: int = 9):
    return {"square": num ** 2}  # Returns the square of the number provided (defaults to 9 if no number is given)

# Check if a number is even or odd
@app.get("/evenodd/{num}")
def evenodd(num: int):
    if num % 2 == 0:
        return {"message": f"{num} is even"}  # Returns a message saying the number is even
    else:
        return {"message": f"{num} is odd"}  # Returns a message saying the number is odd

# Return user information with optional query parameters for age and city
@app.get("/users/{num}")
@app.get("/users")
def userinfo(age: int = 24, city: str = "atp"):
    return {"message": f"User's age is {age} and city={city}"}  # Returns the age and city of the user

# Repeat a given message a specified number of times (query params)
@app.get("/repeat")
def repeat(msg: str, times: int):
    return {"repeat": msg * times}  # Repeats the message 'times' times

# Concatenate first and last name to get full name
@app.get("/fullname")
def fullname(first: str, last: str):
    return {"fullname": first + last}  # Returns the concatenation of the first and last name

# Convert a given string to uppercase
@app.get("/uppercase")
def upper(word: str):
    return {"upper case word": word.upper()}  # Returns the word in uppercase

# Calculate the area of a triangle (length and breadth as query params)
@app.get("/area_of_triangle")
def area_of_triangle(length: int, breadth: int):
    return {"area of triangle": length * breadth}  # Returns the area (length * breadth)

# Calculate the user's age next year
@app.get("/age_next_year/{age}")
def age_next_year(age: int = 24):
    return {"age next year is": age + 1}  # Returns the user's age next year (current age + 1)

# Check if a character is present in a word (query params)
@app.get("/char_contains_in_word")
def char_contains_in_word(word: str, char: str):
    if char in word:
        return {f"{char} is in word"}  # Returns a message confirming the character is in the word
    else:
        return {f"{char} is not in word"}  # Returns a message confirming the character is not in the word

# Combine path and query parameters to display a movie name, year, and rating
@app.get("/movie/{name}")
def movie(name: str, year: int = 2009, rating: int = 9):
    return {"message": f"{name} {year} {rating}"}  # Returns movie details (name, year, rating)

# Return a list of numbers passed in the query (query param as a list of integers)
from fastapi import Query

@app.get("/nums")
def get_nums(num1: list[int] = Query(...)):
    return {"message": f"numbers: {num1}"}  # Returns a list of numbers provided as a query parameter

# Show a substring of a given string (start and end indices as query params)
@app.get("/substring_of_a_string")
def substring(name: str, start: int, end: int):
    return {"message": f"{name[start:end]}"}  # Returns the substring from 'start' to 'end' indices

# Validate a password: should be alphanumeric and exactly 10 characters
@app.get("/validate")
def validate(password: str):
    if password.isalnum() and len(password) == 10:
        return {"message": f"{password} is valid"}  # Returns a message if the password is valid
    else:
        return {"message": f"{password} is invalid"}  # Returns a message if the password is invalid

# Convert Celsius to Fahrenheit (query param)
@app.get("/temperature/{celcius}")
def temperature(celcius: int):
    return {"message": f"celsius {celcius}"}  # Returns the given Celsius temperature

# Task with priority (room as path parameter, priority as query parameter)
@app.get("/task/{room}")
def check(room: str, priority: str = "high"):
    return {"message": f"{room} with {priority} priority"}  # Returns room and priority details

# Reverse a given text (query param)
@app.get("/reverse")
def reverse(text: str):
    return {"message": f"{text[::-1]}"}  # Returns the reversed string of the given text

# Multiply two numbers (with a default second number of 9)
@app.get("/mul/{num}")
def multiply(n1: int, n2: int = 9):
    return {"message": f"product: {n1 * n2}"}  # Returns the product of the two numbers

# Check age eligibility (for age >= 18)
@app.get("/eligible")
def eligibility(age: int):
    if age >= 18:
        return {"message": f"{age} is eligible"}  # Returns a message confirming eligibility
    else:
        return {"message": f"{age} is not eligible"}  # Returns a message saying not eligible



# 1. Home Route (/)

# Request: /

# {
#   "message": "fast api demo"
# }

# 2. Greet User (/greet/{name})

# Request: /greet/John

# {
#   "message": "Good morning, John"
# }

# 3. Addition (/add)

# Request: /add?num1=5&num2=10&num3=15

# {
#   "sum": 30
# }

# 4. Square (/square or /square/{num})

# Request: /square/5

# {
#   "square": 25
# }


# Request: /square

# {
#   "square": 81  # Default is 9, so 9^2 = 81
# }

# 5. Even/Odd (/evenodd/{num})

# Request: /evenodd/7

# {
#   "message": "7 is odd"
# }


# Request: /evenodd/8

# {
#   "message": "8 is even"
# }

# 6. User Info (/users)

# Request: /users?age=25&city=NewYork

# {
#   "message": "User's age is 25 and city=NewYork"
# }


# Request: /users

# {
#   "message": "User's age is 24 and city=atp"  # Default age is 24 and default city is "atp"
# }

# 7. Repeat Message (/repeat)

# Request: /repeat?msg=Hello&times=3

# {
#   "repeat": "HelloHelloHello"
# }

# 8. Full Name (/fullname)

# Request: /fullname?first=John&last=Doe

# {
#   "fullname": "JohnDoe"
# }

# 9. Uppercase (/uppercase)

# Request: /uppercase?word=hello

# {
#   "upper case word": "HELLO"
# }

# 10. Area of Triangle (/area_of_triangle)

# Request: /area_of_triangle?length=5&breadth=10

# {
#   "area of triangle": 50
# }

# 11. Age Next Year (/age_next_year)

# Request: /age_next_year/25

# {
#   "age next year is": 26
# }


# Request: /age_next_year

# {
#   "age next year is": 25  # Default age is 24, so 24 + 1 = 25
# }

# 12. Character in Word (/char_contains_in_word)

# Request: /char_contains_in_word?word=hello&char=e

# {
#   "e is in word": {}
# }


# Request: /char_contains_in_word?word=hello&char=z

# {
#   "z is not in word": {}
# }

# 13. Movie Info (/movie/{name})

# Request: /movie/Inception?year=2010&rating=9

# {
#   "message": "Inception 2010 9"
# }


# Request: /movie/Avatar

# {
#   "message": "Avatar 2009 9"  # Default year is 2009, default rating is 9
# }

# 14. List of Numbers (/nums)

# Request: /nums?num1=1&num1=2&num1=3

# {
#   "message": "numbers: [1, 2, 3]"
# }

# 15. Substring (/substring_of_a_string)

# Request: /substring_of_a_string?name=HelloWorld&start=0&end=5

# {
#   "message": "Hello"
# }


# Request: /substring_of_a_string?name=HelloWorld&start=3&end=8

# {
#   "message": "loWor"
# }

# 16. Password Validation (/validate)

# Request: /validate?password=abc1234567

# {
#   "message": "abc1234567 is valid"
# }


# Request: /validate?password=abc123

# {
#   "message": "abc123 is invalid"
# }

# 17. Temperature (/temperature/{celcius})

# Request: /temperature/25

# {
#   "message": "celsius 25"
# }

# 18. Task Priority (/task/{room})

# Request: /task/Room101?priority=high

# {
#   "message": "Room101 with high priority"
# }


# Request: /task/Room102

# {
#   "message": "Room102 with high priority"  # Default priority is high
# }

# 19. Reverse Text (/reverse)

# Request: /reverse?text=hello

# {
#   "message": "olleh"
# }

# 20. Multiply (/mul/{num})

# Request: /mul/5?n1=3

# {
#   "message": "product: 45"  # Default value for n2 is 9, so 5 * 9 = 45
# }


# Request: /mul/5?n1=3&n2=4

# {
#   "message": "product: 12"  # n1 = 3, n2 = 4, so 3 * 4 = 12
# }

# 21. Age Eligibility (/eligible)

# Request: /eligible?age=20

# {
#   "message": "20 is eligible"
# }


# Request: /eligible?age=17

# {
#   "message": "17 is not eligible"
# }
