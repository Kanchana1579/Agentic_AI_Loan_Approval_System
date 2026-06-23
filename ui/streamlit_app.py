import streamlit as st
import requests

st.title(
    " Agentic AI Loan Approval System"
)

applicant_id = st.text_input("Applicant_ID")

age = age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=28,
    step=1
)

income = st.number_input("Annual Income")

employment = st.selectbox(
    "Employment Type",
    ["Permanent","Contract"]
)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=750,
    step=1
)

loan_amount = st.number_input(
    "Loan Amount"
)

liabilities = st.number_input(
    "Existing Liabilities"
)

if st.button("Submit"):

    payload = {
        "applicant_id": applicant_id,
        "age": age,
        "annual_income": income,
        "employment_type": employment,
        "credit_score": credit_score,
        "loan_amount": loan_amount,
        "existing_liabilities": liabilities
    }

    response = requests.post(
        "http://localhost:8000/loan/evaluate",
        json=payload
    )

    st.write("Status Code:", response.status_code)

    try:
        data = response.json()
        st.json(data)
    except Exception:
        st.error("Backend did not return JSON")
        st.text(response.text)