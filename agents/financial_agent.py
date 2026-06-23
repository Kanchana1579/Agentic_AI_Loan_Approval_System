from mcp_servers.risk_rules_db import evaluate_risk


class FinancialRiskAgent:

    def analyze(self, data):

        return evaluate_risk(
            annual_income=data["annual_income"],
            liabilities=data["existing_liabilities"],
            loan_amount=data["loan_amount"],
            credit_score=data["credit_score"]
        )