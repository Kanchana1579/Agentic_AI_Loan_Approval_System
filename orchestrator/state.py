from typing import TypedDict

class LoanState(TypedDict, total=False):

    applicant_data: dict

    profile: dict

    risk: dict

    decision: dict

    compliance: dict

    human_review: dict

    error: str