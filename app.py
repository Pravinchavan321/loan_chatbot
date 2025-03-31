from flask import Flask, request, jsonify
import os

# Use Bard API or OpenAI API
os.environ["_BARD_API_KEY"] = "your_bard_api_key_here"

app = Flask(__name__)

# Loan eligibility rules
def check_eligibility(age, income, employment_status, credit_score):
    if age < 18:
        return "You must be at least 18 years old."
    if income < 2000:
        return "Your income is too low for a loan."
    if employment_status.lower() not in ["employed", "self-employed"]:
        return "You need a stable job for a loan."
    if credit_score and credit_score < 600:
        return "Your credit score is too low for a loan."

    return "Congratulations! You are eligible for a loan."

@app.route("/check-loan", methods=["POST"])
def loan_checker():
    data = request.json
    age = data.get("age")
    income = data.get("income")
    employment_status = data.get("employment_status")
    credit_score = data.get("credit_score", None)

    result = check_eligibility(age, income, employment_status, credit_score)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
from pyngrok import ngrok

# Start ngrok tunnel on port 5000
public_url = ngrok.connect(5000)
print("Public URL:", public_url)
