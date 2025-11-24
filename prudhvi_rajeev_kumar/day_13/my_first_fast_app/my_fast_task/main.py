from fastapi import FastAPI

# Initialize the FastAPI app instance with the title "FastAPI Example".
app = FastAPI()

# Endpoint to greet the user by name.
# Takes a string 'name' as a path parameter and returns a personalized greeting message.
@app.get("/greet/{name}")
def greet(name: str):
    # Returns a dictionary with a greeting message that includes the name.
    return {"message": f"Hi {name}"}

# Endpoint to calculate the square of a number.
# Takes an integer 'num' as a path parameter and returns the square of the number.
@app.get("/square/{num}")
def square(a: int):
    # Returns a dictionary with the square of the input number.
    return {"message": f"The square is {a*a}"}

# Endpoint to check if a number is even or odd.
# Takes an integer 'num' as a path parameter and returns whether the number is even or odd.
@app.get("/is_even_or_odd/{num}")
def is_even_or_odd(a: int):
    # Checks if the number is even or odd and returns the appropriate message.
    if a % 2 == 0:
        return {"message": "even"}
    else:
        return {"message": "odd"}

# Endpoint to calculate the sum of two integers.
# Takes two integers, 'a' and 'b', as query parameters and returns their sum.
@app.get("/calc_sum")
def calc_sum(a: int, b: int):
    # Returns a dictionary with the sum of 'a' and 'b'.
    return {"message": f"Sum is {a + b}"}

# Endpoint to accept an optional city parameter and return the city name.
# If no city is passed, it defaults to an empty string.
@app.get("/optional_city")
def optional_city(city: str):
    # If 'city' is provided, it returns the city; otherwise, it returns an empty string.
    return {"message": f"City -> {city}" if city else ""}

# Sample Responses Section:

# 1. Sample response when greeting a user by name:
# GET /greet/{name}
# Request (name = "Alice"):
# {
#   "name": "Alice"
# }

# Response:
# {
#   "message": "Hi Alice"
# }

# 2. Sample response when calculating the square of a number:
# GET /square/{num}
# Request (num = 4):
# {
#   "num": 4
# }

# Response:
# {
#   "message": "The square is 16"
# }

# 3. Sample response when checking if a number is even or odd:
# GET /is_even_or_odd/{num}
# Request (num = 5):
# {
#   "num": 5
# }

# Response:
# {
#   "message": "odd"
# }

# 4. Sample response when calculating the sum of two numbers:
# GET /calc_sum
# Request (a = 10, b = 5):
# {
#   "a": 10,
#   "b": 5
# }

# Response:
# {
#   "message": "Sum is 15"
# }

# 5. Sample response when passing a city as a query parameter:
# GET /optional_city
# Request (city = "Paris"):
# {
#   "city": "Paris"
# }

# Response:
# {
#   "message": "City -> Paris"
# }

# 6. Sample response when no city is passed (i.e., empty string):
# GET /optional_city
# Request (city = ""):
# {
#   "city": ""
# }

# Response:
# {
#   "message": ""
# }
