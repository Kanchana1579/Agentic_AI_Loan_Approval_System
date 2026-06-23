from mcp_servers.decision_db import synthesize_decision


class DecisionAgent:

    def decide(
        self,
        profile,
        risk
    ):

        return synthesize_decision(
            profile_score=profile["profile_score"],
            risk_score=risk["risk_score"],
            overall_risk=risk["overall_risk"],
            anomalies=risk["anomalies"]
        )