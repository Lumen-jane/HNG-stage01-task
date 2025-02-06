from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import math

app = FastAPI()

# Enable CORS to allow frontend to fetch data from the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any domain (adjust if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Serve the HTML page
@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

# API endpoint to classify a number
@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="Enter a number to analyze")):
    properties = {
        "number": number,
        "is_prime": is_prime(number),
        "is_even": number % 2 == 0,
        "is_armstrong": is_armstrong(number),
        "fun_fact": f"{number} is cool because it's {'prime' if is_prime(number) else 'not prime'}!"
    }
    return properties
