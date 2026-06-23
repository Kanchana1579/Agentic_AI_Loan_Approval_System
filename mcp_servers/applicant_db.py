from fastmcp import FastMCP

app = FastMCP("ApplicantDB")


@app.tool()
def get_applicant_profile(
    applicant_id: str,
    annual_income: float,
    employment_type: str,
    credit_score: int
):

    profile_score = 0

    scoring_breakdown = {}

    # Income Score
    if annual_income >= 1500000:
        income_score = 40
        income_rating = "Excellent"

    elif annual_income >= 800000:
        income_score = 25
        income_rating = "Good"

    else:
        income_score = 10
        income_rating = "Average"

    profile_score += income_score

    # Employment Score
    if employment_type == "Permanent":
        employment_score = 30
        employment_risk = "Low"

    else:
        employment_score = 15
        employment_risk = "Medium"

    profile_score += employment_score

    # Credit Score
    if credit_score >= 750:
        credit_points = 30
        credit_profile = "Excellent"

    elif credit_score >= 650:
        credit_points = 20
        credit_profile = "Good"

    else:
        credit_points = 10
        credit_profile = "Fair"

    profile_score += credit_points

    return {

        "applicant_id": applicant_id,

        "profile_score": profile_score,

        "income_stability": income_rating,

        "employment_risk": employment_risk,

        "credit_summary": {

            "credit_score": credit_score,

            "credit_profile": credit_profile,

            "history_length_years": 5,

            "delinquencies": 0
        },

        "scoring_breakdown": {

            "income": income_score,

            "employment": employment_score,

            "credit": credit_points
        }
    }


if __name__ == "__main__":
    app.run()