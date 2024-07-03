import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "gender": 1,
    "married": 1,
    "dependents": 2,
    "education": 1,
    "self_employed": 0,
    "applicant_income": 5000,
    "coapplicant_income": 2000,
    "loan_amount": 150,
    "loan_amount_term": 360,
    "credit_history": 1,
    "property_area": 2
}

response = requests.post(url, json=data)
print(response.json())
