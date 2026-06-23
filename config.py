import os
from dotenv import load_dotenv

load_dotenv()

LLMGW_API_KEY = os.getenv("LLMGW_API_KEY")
LLMGW_BASE_URL = os.getenv("LLMGW_BASE_URL")

AGENT_MODELS = {
    "decision_agent": os.getenv("DECISION_AGENT_MODEL"),
    "compliance_agent": os.getenv("COMPLIANCE_AGENT_MODEL")
}

MAX_TOKENS = {
    "decision_agent": 1000,
    "compliance_agent": 500
}