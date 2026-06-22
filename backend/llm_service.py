import os
import json

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def get_loan_decision(profile, risk):

    prompt = f"""
You are a banking loan officer.

Applicant Profile:
{profile}

Risk Analysis:
{risk}

Return ONLY valid JSON:

{{
  "decision":"",
  "risk_score":"",
  "confidence":"",
  "reasoning":""
}}
"""

    response = client.messages.create(
        model="claude-sonnet-4-0",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return json.loads(response.content[0].text)