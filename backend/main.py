from fastapi import FastAPI
from backend.models import LoanApplication
from orchestrator.loan_graph import process_loan

app = FastAPI()

@app.post("/loan/evaluate")
def evaluate(application: LoanApplication):

    result = process_loan(
        application.dict()
    )

    return result