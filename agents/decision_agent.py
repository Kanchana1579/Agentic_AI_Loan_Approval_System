class DecisionAgent:

    def decide(self, profile, risk ):

        if (
            profile["profile_score"] >= 80
            and risk["risk"] == "Low"
        ):
            return {
                "decision": "Approved",
                "risk_score": 10,
                "confidence": "95%",
                "reasoning": "Strong profile and low risk."
            }

        elif risk["risk"] == "High":
            return {
                "decision": "Rejected",
                "risk_score": 80,
                "confidence": "90%",
                "reasoning": "High financial risk."
            }

        return {
            "decision": "Manual Review",
            "risk_score": 50,
            "confidence": "70%",
            "reasoning": "Requires human review."
        }