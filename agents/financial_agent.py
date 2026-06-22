class FinancialRiskAgent:

    def analyze(self, data):

        income = data.get("annual_income", 0)
        liabilities = data.get("existing_liabilities", 0)

        if income == 0:
            return {
                "dti": 1,
                "risk": "High"
            }

        dti = liabilities / income

        risk = "Low"

        if dti > 0.5:
            risk = "High"

        return {
            "dti": dti,
            "risk": risk
        }