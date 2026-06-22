from database.db import SessionLocal
from database.models import AuditLog

def save_audit(
    applicant_id,
    decision,
    confidence,
    reasoning
):

    db = SessionLocal()

    record = AuditLog(
        applicant_id=applicant_id,
        decision=decision,
        confidence=confidence,
        reasoning=reasoning
    )

    db.add(record)
    db.commit()
    db.close()