# **Number Classification API**

A Python-based API that takes a number as input and returns its mathematical properties, along with a fun fact.

## **Features**
This API provides the following features:
- **Prime Check**: Determines if the number is a prime number.
- **Armstrong Check**: Checks if the number is an Armstrong number.
- **Perfect Check**: Identifies if the number is a perfect number.
- **Odd/Even Check**: Indicates whether the number is odd or even.
- **Digit Sum**: Calculates the sum of the digits of the number.
- **Fun Fact**: Fetches a fun fact about the number from the Numbers API.

---

## **Endpoints**

### **GET `/api/classify-number`**

#### **Query Parameter**
- `number` (required): An integer value to classify.

#### **Response Formats**
1. **Success (200 OK)**
    ```json
    {
        "number": 371,
        "is_prime": false,
        "is_perfect": false,
        "properties": ["armstrong", "odd"],
        "digit_sum": 11,
        "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
    }
    ```

2. **Error (400 Bad Request)**
    ```json
    {
        "number": "alphabet",
        "error": true
    }
    ```

---

## **Setup and Installation**

### **Clone the Repository**
cd <Desktop/DevOps_Stage1/number-classification-api>
Initialized git and cloned the repository to my local repository on git bash terminal (VSCode):
```bash
git init
git remote add origin clone https://github.com/https://github.com/Chinenye-Consults/Number_Classification_API.git
git branch -M main
git config user.name "Chinenye-Consults"
git config user.email "chinenyeobasi4u@gmail.com"
```

### **Install Dependencies**
Install the required dependencies using `pip`:
```bash
pip install fastapi uvicorn requests
```

### **Run the Application**
Start the FastAPI application using Uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

The API was is available at `http://127.0.0.1:8000`.

---

## **Deployment**
This API has been deployed and is publicly accessible at:
- **Base URL**: `<http://127.0.0.1:8080/api/classify-number?number=371>`


## **Code Structure**
The project has a well-organized code structure for maintainability:
```
.
├── main.py                 # Main application logic
├── utils.py                # Utility functions (prime, Armstrong, perfect checks, etc.)
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignore file
```

---

## **Technology Stack**
- **Programming Language**: Python 3.13.1
- **Framework**: FastAPI
- **Deployment**: Google Cloud Platform (GCP)
- **External API**: 371 (Fun facts: 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.")
- **Package Manager**: pip

---

## **API Features in Detail**

### **Mathematical Properties**
1. **Prime**: Checks if the number is divisible only by 1 and itself.
2. **Armstrong**: Verifies if the number is equal to the sum of its digits each raised to the power of the number of digits (e.g., 371 = \(3^3 + 7^3 + 1^3\)).
3. **Perfect**: Validates if the number equals the sum of its proper divisors (excluding itself).
4. **Odd/Even**: Determines if the number is odd or even.
5. **Digit Sum**: Adds all the digits of the number.

### **Fun Fact**
The Numbers API is used to fetch a fun fact related to the number, enriching the response with contextual and historical insights.

---

## **Error Handling**
- **Invalid Input**: Returns a `400 Bad Request` with a descriptive error message if the input is not a valid integer.
    ```json
    {
        "number": "alphabet",
    "error": true
    }
    ```

---

## **Testing**
1. Tested with valid numbers:
   - `http://127.0.0.1:8080/api/classify-number?number=371`
2. Tested with invalid inputs:
   - `http://127.0.0.1:8080/api/classify-number?number=abc`
3. Tested edge cases:
   - Negative numbers
   - Large integers
   - Zero

---

## **License**
This project is open-source and available under the [MIT License](LICENSE).
MIT License

Copyright (c) [2025] [Chinenye_Obasi]

---

## **Contributions**
Contributions are welcome! Kindly follow these steps to contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## **Contact**
For questions or suggestions, feel free to contact:
- **Email**: chinenyeobasi4u@gmail.com
- **GitHub**: https://github.com/Chinenye-Consults
