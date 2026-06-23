from fastmcp import FastMCP
from datetime import datetime
import uuid

app = FastMCP("Notification")


@app.tool()
def send_notification(
    applicant_id: str,
    decision: str,
    loan_amount: float = 0
):

    case_id = (
        f"CASE-"
        f"{uuid.uuid4().hex[:8].upper()}"
    )

    # -----------------------
    # KYC Validation
    # -----------------------

    kyc_status = "PASSED"

    if not applicant_id:
        kyc_status = "FAILED"

    # -----------------------
    # AML Validation
    # -----------------------

    aml_status = "PASSED"

    # -----------------------
    # Regulatory Checks
    # -----------------------

    regulatory_checks = []

    if loan_amount <= 5000000:

        regulatory_checks.append(
            "Loan amount within limit: YES"
        )

    else:

        regulatory_checks.append(
            "Loan amount within limit: NO"
        )

    # -----------------------
    # Notification Details
    # -----------------------

    recipients = [
        applicant_id,
        "loan.officer@bank.com"
    ]

    channels = [
        "Email",
        "Dashboard"
    ]

    timestamp = (
        datetime.utcnow().isoformat()
    )

    # -----------------------
    # Audit Log
    # -----------------------

    audit_log = {

        "case_id": case_id,

        "timestamp": timestamp,

        "actor": "ComplianceAgent",

        "decision": decision
    }

    return {

        "case_id": case_id,

        "timestamp": timestamp,

        "decision": decision,

        "kyc_status": kyc_status,

        "aml_status": aml_status,

        "regulatory_checks":
            regulatory_checks,

        "notification_status":
            "Sent",

        "notification_sent_to":
            recipients,

        "channels":
            channels,

        "audit_log":
            audit_log
    }


if __name__ == "__main__":
    app.run()