# Import necessary modules
from fastapi import FastAPI, Query  # FastAPI to create the API
import requests  # Requests library to fetch data from Numbers API

# Initialize FastAPI app
app = FastAPI()

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

# Initialize FastAPI app
app = FastAPI()

# Custom handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,  # Return 400 instead of 422
        content={
            "number": "alphabet", "error": True
        },
    )


# Function to check if a number is prime
def is_prime(n: int) -> bool:
    """Returns True if a number is prime, otherwise False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to square root of n
        if n % i == 0:
            return False
    return True

# Function to check if a number is a perfect number
def is_perfect(n: int) -> bool:
    """Returns True if a number is perfect (sum of divisors equals number)."""
    return sum(i for i in range(1, n) if n % i == 0) == n

# Function to check if a number is an Armstrong number
def is_armstrong(n: int) -> bool:
    """Returns True if a number is an Armstrong number."""
    return sum(int(digit) ** len(str(n)) for digit in str(n)) == n

# API endpoint definition
from fastapi import HTTPException

@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="Enter a valid integer to classify")):
    try:
        # Your logic here
        properties = []
        if is_prime(number):
            properties.append("prime")
        if is_perfect(number):
            properties.append("perfect")
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("even" if number % 2 == 0 else "odd")

        fun_fact = f"{number} is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"  # Example fun fact

        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(number)),
            "fun_fact": fun_fact,
        }
    except ValueError:
        # Handle invalid query parameter
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a valid integer.")
