# Import necessary modules
from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Custom handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,  
        content={"number": "alphabet", "error": True},  # Required error format
    )

# Function to check if a number is prime
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is a perfect number
def is_perfect(n: float) -> bool:
    if n < 1 or not n.is_integer():  # Ensure it's a positive whole number
        return False
    n = int(n)  # Convert to integer
    return sum(i for i in range(1, n) if n % i == 0) == n

# Function to check if a number is an Armstrong number
def is_armstrong(n: float) -> bool:
    if not n.is_integer():  # Armstrong numbers apply to whole numbers
        return False
    n = int(n)
    return sum(int(digit) ** len(str(n)) for digit in str(n)) == n

# API endpoint definition
@app.get("/api/classify-number")
async def classify_number(number: float = Query(..., description="Enter a valid number to classify")):
    try:
        properties = []
        number_is_int = number.is_integer()  # Check if it's a whole number

        if number_is_int:  # Check only for whole numbers
            number = int(number)
            if is_prime(number):
                properties.append("prime")
            if is_perfect(number):
                properties.append("perfect")
            if is_armstrong(number):
                properties.append("armstrong")
            properties.append("even" if number % 2 == 0 else "odd")

        response = {
            "number": number,
            "is_prime": is_prime(int(number)) if number_is_int else False,
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(abs(int(number)))) if number_is_int else None,
            "fun_fact": f"{number} is an Armstrong number because {'+'.join([f'{digit}^{len(str(number))}' for digit in str(number)])} = {number}"
            if "armstrong" in properties else None,
        }

        return response
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": "alphabet", "error": True})  # Required error format
