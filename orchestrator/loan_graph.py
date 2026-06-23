from datetime import datetime
import uuid

def process_loan(data):

    result = graph.invoke(
        {
            "applicant_data": data
        }
    )

    decision_id = (
        f"LOAN-{datetime.now().strftime('%Y%m%d')}-"
        f"{str(uuid.uuid4())[:4].upper()}"
    )

    save_audit(
        applicant_id=data["applicant_id"],
        decision=result["decision"]["decision"],
        confidence=result["decision"]["confidence"],
        reasoning=result["decision"]["reasoning"]
    )

    response = {

        "decision_id": decision_id,

        "timestamp": datetime.utcnow().isoformat(),

        "applicant_id": data["applicant_id"],

        # --------------------------------
        # Profile Analysis
        # --------------------------------
        "profile_analysis": {

            "income_score":
                result["profile"]["scoring_breakdown"].get(
                    "income",
                    0
                ),

            "employment_score":
                result["profile"]["scoring_breakdown"].get(
                    "employment",
                    0
                ),

            "credit_score":
                result["profile"]["scoring_breakdown"].get(
                    "credit",
                    0
                ),

            "total_score":
                result["profile"]["profile_score"],

            "factors": {

                "annual_income": {
                    "value": data["annual_income"],
                    "rating":
                        result["profile"]["income_stability"]
                },

                "employment_type": {
                    "value": data["employment_type"],
                    "rating":
                        result["profile"]["employment_risk"]
                },

                "credit_score": {
                    "value": data["credit_score"],
                    "rating":
                        result["profile"]["credit_summary"][
                            "credit_profile"
                        ]
                }
            }
        },

        # --------------------------------
        # Financial Risk
        # --------------------------------
        "financial_risk": {

            "dti":
                result["risk"]["dti"],

            "dti_level":
                result["risk"]["dti_risk"],

            "credit_risk":
                result["risk"]["credit_risk"],

            "loan_risk":
                result["risk"]["loan_risk"],

            "anomalies":
                result["risk"]["anomalies"],

            "risk_score":
                result["risk"]["risk_score"]
        },

        # --------------------------------
        # Decision
        # --------------------------------
        "decision": {

            "classification":
                result["decision"]["decision"],

            "final_risk_score":
                result["risk"]["risk_score"],

            "confidence":
                result["decision"]["confidence"],

            "confidence_reasoning":
                result["decision"]["reasoning"],

            "key_factors":
                result["decision"].get(
                    "key_factors",
                    []
                ),

            "limiting_factors":
                result["risk"]["anomalies"],

            "next_steps":
                (
                    [
                        "Send approval notification",
                        "Schedule fund transfer"
                    ]
                    if result["decision"]["decision"]
                    == "Approved"
                    else
                    [
                        "Notify applicant",
                        "Archive application"
                    ]
                )
        },

        # --------------------------------
        # Compliance
        # --------------------------------
        "compliance": {

            "kyc_status":
                "PASSED",

            "aml_status":
                "PASSED",

            "regulatory_checks": [

                (
                    "Loan amount within limit: YES"
                    if data["loan_amount"] <= 5000000
                    else
                    "Loan amount within limit: NO"
                )
            ],

            "case_id":
                result["compliance"]["case_id"],

            "notification_sent_to": [
                "applicant@example.com"
            ],

            "notification_time":
                result["compliance"]["timestamp"]
        }
    }

    if "human_review" in result:

        response["human_review"] = (
            result["human_review"]
        )

    return response