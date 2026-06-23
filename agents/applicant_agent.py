class ApplicantAgent:

    def analyze(self, data):

        score = 0

        scoring_breakdown = {}

        # --------------------
        # Income Stability
        # --------------------
        annual_income = data["annual_income"]

        if annual_income >= 1500000:
            income_score = 40
            income_stability = "High"

        elif annual_income >= 800000:
            income_score = 25
            income_stability = "Medium"

        else:
            income_score = 10
            income_stability = "Low"

        score += income_score

        scoring_breakdown["income"] = income_score

        # --------------------
        # Employment Risk
        # --------------------
        employment_type = data["employment_type"]

        if employment_type == "Permanent":

            employment_score = 30
            employment_risk = "Low"

        elif employment_type == "Contract":

            employment_score = 15
            employment_risk = "Medium"

        else:

            employment_score = 5
            employment_risk = "High"

        score += employment_score

        scoring_breakdown["employment"] = employment_score

        # --------------------
        # Credit Profile
        # --------------------
        credit_score = data["credit_score"]

        if credit_score >= 750:

            credit_points = 30
            credit_profile = "Excellent"

        elif credit_score >= 650:

            credit_points = 20
            credit_profile = "Good"

        elif credit_score >= 550:

            credit_points = 10
            credit_profile = "Fair"

        else:

            credit_points = 0
            credit_profile = "Poor"

        score += credit_points

        scoring_breakdown["credit"] = credit_points

        # --------------------
        # Application Validation
        # --------------------
        missing_fields = []

        required_fields = [
            "applicant_id",
            "annual_income",
            "employment_type",
            "credit_score",
            "loan_amount"
        ]

        for field in required_fields:

            if field not in data:
                missing_fields.append(field)

        application_complete = len(missing_fields) == 0

        # --------------------
        # Credit Summary
        # --------------------
        credit_summary = {
            "credit_score": credit_score,
            "credit_profile": credit_profile,
            "history_length_years": 5,
            "delinquencies": 0
        }

        # --------------------
        # Final Response
        # --------------------
        return {

            "profile_score": score,

            "income_stability": income_stability,

            "employment_risk": employment_risk,

            "credit_summary": credit_summary,

            "application_complete": application_complete,

            "missing_fields": missing_fields,

            "scoring_breakdown": scoring_breakdown
        }