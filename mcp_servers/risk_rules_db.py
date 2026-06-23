from fastmcp import FastMCP

app = FastMCP("RiskRules")


@app.tool()
def evaluate_risk(
    annual_income: float,
    liabilities: float,
    loan_amount: float,
    credit_score: int
):

    anomalies = []

    # -------------------------
    # Validation
    # -------------------------

    if annual_income <= 0:

        return {
            "overall_risk": "High",
            "risk_score": 100,
            "reasoning": "Income cannot be zero.",
            "anomalies": [
                "Invalid annual income"
            ]
        }

    # -------------------------
    # Debt To Income
    # -------------------------

    dti = liabilities / annual_income

    if dti <= 0.30:
        dti_risk = "Low"

    elif dti <= 0.50:
        dti_risk = "Medium"

    else:
        dti_risk = "High"

    # -------------------------
    # Credit Risk
    # -------------------------

    if credit_score >= 750:
        credit_risk = "Low"

    elif credit_score >= 650:
        credit_risk = "Medium"

    else:
        credit_risk = "High"

    # -------------------------
    # Loan To Income
    # -------------------------

    loan_to_income = loan_amount / annual_income

    if loan_to_income <= 0.30:
        loan_risk = "Low"

    elif loan_to_income <= 0.60:
        loan_risk = "Medium"

    else:
        loan_risk = "High"

    # -------------------------
    # Anomaly Detection
    # -------------------------

    if loan_amount > annual_income * 2:

        anomalies.append(
            "Requested loan exceeds 2x annual income"
        )

    if credit_score < 500:

        anomalies.append(
            "Very low credit score"
        )

    if liabilities > annual_income:

        anomalies.append(
            "Liabilities exceed annual income"
        )

    # -------------------------
    # Composite Risk Score
    # -------------------------

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

    # -------------------------
    # Overall Risk
    # -------------------------

    if risk_score <= 35:

        overall_risk = "Low"

    elif risk_score <= 70:

        overall_risk = "Medium"

    else:

        overall_risk = "High"

    # -------------------------
    # Recommendations
    # -------------------------

    recommendations = []

    if dti_risk != "Low":

        recommendations.append(
            "Reduce liabilities before loan approval."
        )

    if credit_risk != "Low":

        recommendations.append(
            "Improve credit score."
        )

    if loan_risk != "Low":

        recommendations.append(
            "Consider lower loan amount."
        )

    # -------------------------
    # Reasoning
    # -------------------------

    reasoning = (
        f"DTI={dti:.2f} ({dti_risk}), "
        f"Credit Risk={credit_risk}, "
        f"Loan Ratio={loan_to_income:.2f} ({loan_risk})."
    )

    return {

    "dti": round(dti, 2),

    "dti_level": dti_risk,

    "dti_risk": dti_risk,

    "credit_risk": credit_risk,

    "loan_to_income": round(
        loan_to_income,
        2
    ),

    "loan_risk": loan_risk,

    "overall_risk": overall_risk,

    "risk_score": risk_score,

    "risk_breakdown": {

        "dti_component":
            dti_risk,

        "credit_component":
            credit_risk,

        "loan_component":
            loan_risk
    },

    "anomalies": anomalies,

    "reasoning": reasoning,

    "recommendations":
        recommendations
}

if __name__ == "__main__":
    app.run()