from mcp_servers.applicant_db import get_applicant_profile

class ApplicantAgent:

    def analyze(self, data):

        return get_applicant_profile(
            applicant_id=data["applicant_id"],
            annual_income=data["annual_income"],
            employment_type=data["employment_type"],
            credit_score=data["credit_score"],
            employment_years=data.get(
                "employment_years",
                3
            ),
            industry=data.get(
                "industry",
                "Technology"
            )
        )