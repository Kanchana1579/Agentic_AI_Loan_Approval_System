class FinancialRiskAgent:

    def analyze(self,data):

        dti = data["existing_liabilities"] / data["annual_income"]

        risk = "Low"

        if dti > 0.5:
            risk = "High"

        return {
            "dti":dti,
            "risk":risk
        }