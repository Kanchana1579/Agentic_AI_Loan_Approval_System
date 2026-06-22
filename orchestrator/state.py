from typing import TypedDict

class LoanState(TypedDict):
    applicant_data: dict
    profile: dict
    risk: dict
    decision: dict
    compliance: dict