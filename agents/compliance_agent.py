from mcp_servers.notification_db import send_notification


class ComplianceAgent:

    def execute(
        self,
        decision,
        applicant_data
    ):

        return send_notification(
            applicant_id=applicant_data["applicant_id"],
            decision=decision["decision"],
            loan_amount=applicant_data["loan_amount"]
        )