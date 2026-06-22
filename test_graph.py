# test_graph.py

from orchestrator.loan_graph import process_loan

result = process_loan(
    {
        "applicant_id":"APPL-001",
        "age":30,
        "annual_income":1200000,
        "employment_type":"Permanent",
        "credit_score":780,
        "loan_amount":300000,
        "existing_liabilities":100000
    }
)

print(result)