from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()

class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)

    applicant_id = Column(String)

    decision = Column(String)

    confidence = Column(String)

    reasoning = Column(Text)