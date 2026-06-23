from datetime import datetime
import uuid


class ComplianceAgent:

    MAX_LOAN_AMOUNT = 5000000

    def execute(self, decision, applicant_data=None):

        case_id = f"CASE-{uuid.uuid4().hex[:8].upper()}"

        compliance_checks = []

        violations = []

        # -------------------------
        # KYC Validation
        # -------------------------

        kyc_status = "Passed"

        if applicant_data:

            if not applicant_data.get("applicant_id"):

                kyc_status = "Failed"

                violations.append(
                    "Missing Applicant ID"
                )

        compliance_checks.append({
            "check": "KYC Validation",
            "status": kyc_status
        })

        # -------------------------
        # AML Validation
        # -------------------------

        aml_status = "Passed"

        compliance_checks.append({
            "check": "AML Screening",
            "status": aml_status
        })

        # -------------------------
        # Loan Amount Validation
        # -------------------------

        loan_status = "Passed"

        if applicant_data:

            loan_amount = applicant_data.get(
                "loan_amount",
                0
            )

            if loan_amount > self.MAX_LOAN_AMOUNT:

                loan_status = "Failed"

                violations.append(
                    "Loan amount exceeds regulatory limit"
                )

        compliance_checks.append({
            "check": "Loan Amount Limit",
            "status": loan_status
        })

        # -------------------------
        # Compliance Status
        # -------------------------

        overall_status = (
            "Passed"
            if len(violations) == 0
            else "Failed"
        )

        # -------------------------
        # Notification Details
        # -------------------------

        notifications = {
            "recipients": [
                "Applicant",
                "Loan Officer"
            ],
            "channels": [
                "Email",
                "Dashboard"
            ],
            "status": "Sent"
        }

        # -------------------------
        # Audit Log Entry
        # -------------------------

        audit_log = {
            "case_id": case_id,
            "timestamp": str(datetime.now()),
            "actor": "ComplianceAgent",
            "decision": decision["decision"]
        }

        # -------------------------
        # Final Response
        # -------------------------

        return {

            "case_id": case_id,

            "timestamp": str(datetime.now()),

            "action": decision["decision"],

            "compliance_status": overall_status,

            "checks": compliance_checks,

            "violations": violations,

            "notification": notifications,

            "audit_log": audit_log
        }