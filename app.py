from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open('loan_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Extract the features from the JSON data
        gender = int(data['gender'])
        married = int(data['married'])
        dependents = int(data['dependents'])
        education = int(data['education'])
        self_employed = int(data['self_employed'])
        applicant_income = int(data['applicant_income'])
        coapplicant_income = float(data['coapplicant_income'])
        loan_amount = float(data['loan_amount'])
        loan_amount_term = float(data['loan_amount_term'])
        credit_history = float(data['credit_history'])
        property_area = int(data['property_area'])

        # Create input data array
        input_data = np.array([[gender, married, dependents, education, self_employed, 
                                applicant_income, coapplicant_income, loan_amount, 
                                loan_amount_term, credit_history, property_area]])

        # Make prediction
        prediction = model.predict(input_data)
        
        # Return the result
        result = 'Loan Approved' if prediction[0] == 1 else 'Loan Not Approved'
        return jsonify({'prediction': result})
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
