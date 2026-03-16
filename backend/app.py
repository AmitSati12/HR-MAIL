from flask import Flask, render_template, request, jsonify
from send_mail import send_email
from db import insert_application
import pandas as pd
import time
from flask_cors import CORS

# app = Flask(__name__)
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend API is running"
@app.route("/")
def health():
    return "Backend running successfully"


@app.route("/bulk_send", methods=["POST"])
def bulk_send():

    file = request.files["file"]
    message = request.form["message"]

    # Read Excel file
    df = pd.read_excel(file)

    # Clean column names (remove spaces, lowercase)
    df.columns = df.columns.str.strip().str.lower()

    print("Columns found:", df.columns)

    sent_count = 0

    for index, row in df.iterrows():

        # Clean values from Excel
        company = str(row["company"]).strip()
        role = str(row["role"]).strip()
        email = str(row["email"]).strip().replace(",", "")

        print(f"Sending email {index+1} to {email}")

        try:

            send_email(email, company, role, message)

            insert_application(company, role, email, message)

            sent_count += 1

            print("Sent successfully")

        except Exception as e:

            print("Error sending to:", email, e)

        # Delay to avoid Gmail spam blocking
        time.sleep(7)

    return jsonify({"status": f"{sent_count} emails sent successfully"})


@app.route("/send", methods=["POST"])
def send():

    company = request.form.get("company")
    role = request.form.get("role")
    hr_email = request.form.get("email")
    message = request.form.get("message")

    print("Company:", company)
    print("Role:", role)
    print("Email:", hr_email)
    print("Message:", message)

    try:

        print("Sending email...")

        send_email(hr_email, company, role, message)

        print("Saving to database...")

        insert_application(company, role, hr_email, message)

        return jsonify({"status": "Email Sent Successfully"})

    except Exception as e:

        print("ERROR:", e)

        return jsonify({"status": str(e)})


if __name__ == "__main__":
    app.run(debug=True)