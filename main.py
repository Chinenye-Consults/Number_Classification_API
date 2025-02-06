from fastapi import FastAPI, Query, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2 or n % 1 != 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number. 0 should NOT be perfect."""
    if n <= 0 or n % 1 != 0:
        return False
    return sum(i for i in range(1, int(n)) if int(n) % i == 0) == int(n)

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    if n % 1 != 0:
        return False
    digits = [int(d) for d in str(abs(int(n)))]
    return sum(d ** len(digits) for d in digits) == abs(int(n))

@app.get("/")
def read_root():
    """Handles requests to the root endpoint with a 400 Bad Request error."""
    raise HTTPException(status_code=400, detail="Invalid endpoint. Use '/api/classify-number'")

@app.get("/api/classify-number")
def classify_number(number: str = Query(..., description="Number to classify")):
    """API Endpoint to classify a number."""
    
    # Validate number format
    if not number.replace(".", "").replace("-", "").isdigit():
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True, "message": "Invalid number format"},
        )
    
    try:
        number = float(number)
        if number % 1 == 0:
            number = int(number)
    except Exception:
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True, "message": "Invalid number format"},
        )

    properties = []
    
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    if is_armstrong(number):
        digits = [int(d) for d in str(abs(int(number)))]
        powers = " + ".join([f"{d}^{len(digits)}" for d in digits])
        fun_fact = f"{number} is an Armstrong number because {powers} = {number}"
    else:
        fun_fact = f"{number} is not an Armstrong number."

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(map(int, str(abs(int(number))))),
        "fun_fact": fun_fact
    }

    return JSONResponse(status_code=200, content=response)

@app.exception_handler(422)
async def validation_exception_handler(request, exc):
    """Ensures invalid inputs return a 400 Bad Request."""
    return JSONResponse(
        status_code=400,
        content={"error": True, "message": "Invalid input. Please provide a valid number."},
    )