from pydantic import BaseModel

class LoanApplication(BaseModel):
    applicant_id:str
    age:int
    annual_income:float
    employment_type:str
    credit_score:int
    loan_amount:float
    existing_liabilities:float