class FinancialRiskAgent:

    def analyze(self, data):

        income = data.get("annual_income", 0)

        liabilities = data.get(
            "existing_liabilities",
            0
        )

        loan_amount = data.get(
            "loan_amount",
            0
        )

        credit_score = data.get(
            "credit_score",
            0
        )

        anomalies = []

        # ---------------------------------
        # Debt-to-Income Ratio
        # ---------------------------------

        if income == 0:

            return {
                "overall_risk": "High",
                "risk_score": 100,
                "reasoning": "Income cannot be zero."
            }

        dti = liabilities / income

        if dti <= 0.30:
            dti_risk = "Low"

        elif dti <= 0.50:
            dti_risk = "Medium"

        else:
            dti_risk = "High"

        # ---------------------------------
        # Credit Risk
        # ---------------------------------

        if credit_score >= 750:
            credit_risk = "Low"

        elif credit_score >= 650:
            credit_risk = "Medium"

        else:
            credit_risk = "High"

        # ---------------------------------
        # Loan-to-Income Ratio
        # ---------------------------------

        loan_to_income = loan_amount / income

        if loan_to_income <= 0.30:
            loan_risk = "Low"

        elif loan_to_income <= 0.60:
            loan_risk = "Medium"

        else:
            loan_risk = "High"

        # ---------------------------------
        # Anomaly Detection
        # ---------------------------------

        if loan_amount > income * 2:

            anomalies.append(
                "Requested loan exceeds 2x annual income"
            )

        if credit_score < 500:

            anomalies.append(
                "Very low credit score"
            )

        if liabilities > income:

            anomalies.append(
                "Liabilities exceed annual income"
            )

        # ---------------------------------
        # Composite Risk Score
        # ---------------------------------

        risk_score = 0

        risk_score += {
            "Low": 10,
            "Medium": 25,
            "High": 40
        }[dti_risk]

        risk_score += {
            "Low": 10,
            "Medium": 25,
            "High": 40
        }[credit_risk]

        risk_score += {
            "Low": 10,
            "Medium": 25,
            "High": 40
        }[loan_risk]

        risk_score = min(
            risk_score,
            100
        )

        # ---------------------------------
        # Overall Risk
        # ---------------------------------

        if risk_score <= 35:

            overall_risk = "Low"

        elif risk_score <= 70:

            overall_risk = "Medium"

        else:

            overall_risk = "High"

        # ---------------------------------
        # Recommendations
        # ---------------------------------

        recommendations = []

        if dti_risk != "Low":

            recommendations.append(
                "Reduce existing liabilities before applying."
            )

        if credit_risk != "Low":

            recommendations.append(
                "Improve credit score for better approval chances."
            )

        if loan_risk != "Low":

            recommendations.append(
                "Consider a lower loan amount."
            )

        # ---------------------------------
        # Explainable Reasoning
        # ---------------------------------

        reasoning = (
            f"DTI ratio is {dti:.2f} "
            f"({dti_risk} risk). "
            f"Credit score is {credit_score} "
            f"({credit_risk} risk). "
            f"Loan-to-income ratio is "
            f"{loan_to_income:.2f} "
            f"({loan_risk} risk)."
        )

        return {

            "dti": round(dti, 2),

            "dti_risk": dti_risk,

            "credit_risk": credit_risk,

            "loan_to_income": round(
                loan_to_income,
                2
            ),

            "loan_risk": loan_risk,

            "anomalies": anomalies,

            "overall_risk": overall_risk,

            "risk_score": risk_score,

            "reasoning": reasoning,

            "recommendations": recommendations
        }