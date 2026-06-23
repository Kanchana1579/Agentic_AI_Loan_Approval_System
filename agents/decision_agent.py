class DecisionAgent:

    APPROVAL_THRESHOLD = 80
    REJECTION_THRESHOLD = 40

    PROFILE_WEIGHT = 0.6
    RISK_WEIGHT = 0.4

    def decide(self, profile, risk):

        profile_score = profile["profile_score"]

        risk_score = risk["risk_score"]

        overall_risk = risk["overall_risk"]

        anomalies = risk["anomalies"]

        # -----------------------------
        # Weighted Decision Score
        # -----------------------------

        decision_score = (
            (profile_score * self.PROFILE_WEIGHT)
            + ((100 - risk_score) * self.RISK_WEIGHT)
        )

        # -----------------------------
        # Confidence Calculation
        # -----------------------------

        confidence = 50

        if profile_score >= 80:
            confidence += 20

        if overall_risk == "Low":
            confidence += 20

        if len(anomalies) == 0:
            confidence += 10

        confidence = min(confidence, 99)

        # -----------------------------
        # Decision Logic
        # -----------------------------

        if (
            decision_score >= self.APPROVAL_THRESHOLD
            and overall_risk == "Low"
        ):

            decision = "Approved"

        elif (
            decision_score <= self.REJECTION_THRESHOLD
            or overall_risk == "High"
        ):

            decision = "Rejected"

        else:

            decision = "Manual Review"

        # -----------------------------
        # Detailed Factor Breakdown
        # -----------------------------

        factors = {
            "profile_score": profile_score,
            "risk_score": risk_score,
            "decision_score": round(decision_score, 2),
            "overall_risk": overall_risk,
            "anomaly_count": len(anomalies)
        }

        # -----------------------------
        # Dynamic Reasoning
        # -----------------------------

        reasoning = (
            f"Profile score of {profile_score} contributed "
            f"{self.PROFILE_WEIGHT*100:.0f}% of the decision. "
            f"Risk score of {risk_score} contributed "
            f"{self.RISK_WEIGHT*100:.0f}% of the decision. "
            f"Overall risk assessment is '{overall_risk}'. "
            f"Detected anomalies: {len(anomalies)}."
        )

        if anomalies:
            reasoning += (
                " Risk indicators include: "
                + ", ".join(anomalies)
            )

        return {

            "decision": decision,

            "confidence": f"{confidence}%",

            "risk_score": risk_score,

            "decision_score": round(
                decision_score,
                2
            ),

            "key_factors": factors,

            "reasoning": reasoning
        }