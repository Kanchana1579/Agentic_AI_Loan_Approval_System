from fastmcp import FastMCP

app = FastMCP("DecisionSynthesis")


@app.tool()
def synthesize_decision(
    profile_score: int,
    risk_score: int,
    overall_risk: str,
    anomalies: list
):

    # -------------------------
    # Configurable Thresholds
    # -------------------------

    APPROVAL_THRESHOLD = 80
    REJECTION_THRESHOLD = 40

    PROFILE_WEIGHT = 0.6
    RISK_WEIGHT = 0.4

    # -------------------------
    # Weighted Decision Score
    # -------------------------

    decision_score = (
        (profile_score * PROFILE_WEIGHT)
        +
        ((100 - risk_score) * RISK_WEIGHT)
    )

    # -------------------------
    # Dynamic Confidence
    # -------------------------

    confidence = 50

    if profile_score >= 80:
        confidence += 20

    if overall_risk == "Low":
        confidence += 20

    if len(anomalies) == 0:
        confidence += 10

    confidence = min(confidence, 99)

    # -------------------------
    # Decision Logic
    # -------------------------

    if (
        decision_score >= APPROVAL_THRESHOLD
        and overall_risk == "Low"
    ):

        decision = "Approved"

    elif (
        decision_score <= REJECTION_THRESHOLD
        or overall_risk == "High"
    ):

        decision = "Rejected"

    else:

        decision = "Manual Review"

    # -------------------------
    # Key Factors
    # -------------------------

    key_factors = [

        f"Profile Score: {profile_score}",

        f"Risk Score: {risk_score}",

        f"Overall Risk: {overall_risk}",

        f"Decision Score: {round(decision_score, 2)}"
    ]

    # -------------------------
    # Reasoning
    # -------------------------

    reasoning = (
        f"Profile score contributed "
        f"{PROFILE_WEIGHT * 100:.0f}% "
        f"to decision calculation. "
        f"Risk score contributed "
        f"{RISK_WEIGHT * 100:.0f}%. "
        f"Overall risk classified as "
        f"{overall_risk}. "
        f"Detected anomalies: "
        f"{len(anomalies)}."
    )

    if anomalies:

        reasoning += (
            " Anomalies detected: "
            + ", ".join(anomalies)
        )

    # -------------------------
    # Next Steps
    # -------------------------

    if decision == "Approved":

        next_steps = [

            "Send approval notification",

            "Schedule fund disbursement"
        ]

    elif decision == "Rejected":

        next_steps = [

            "Notify applicant",

            "Archive application"
        ]

    else:

        next_steps = [

            "Assign to Loan Officer",

            "Perform manual review"
        ]

    return {

        "decision": decision,

        "risk_score": risk_score,

        "decision_score": round(
            decision_score,
            2
        ),

        "confidence": f"{confidence}%",

        "key_factors": key_factors,

        "reasoning": reasoning,

        "next_steps": next_steps
    }


if __name__ == "__main__":
    app.run()