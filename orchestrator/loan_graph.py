from langgraph.graph import StateGraph, END
from agents.applicant_agent import ApplicantAgent
from agents.financial_agent import FinancialRiskAgent
from agents.decision_agent import DecisionAgent
from agents.compliance_agent import ComplianceAgent
from orchestrator.state import LoanState
from database.audit_service import save_audit
from datetime import datetime
import uuid

# ------------------------------------------------

# Agent Initialization

# ------------------------------------------------

applicant_agent = ApplicantAgent()

risk_agent = FinancialRiskAgent()

decision_agent = DecisionAgent()

compliance_agent = ComplianceAgent()

# ------------------------------------------------

# LangGraph Nodes

# ------------------------------------------------

def applicant_node(state):

    state["profile"] = applicant_agent.analyze(
        state["applicant_data"]
    )

    return state


def risk_node(state):


 state["risk"] = risk_agent.analyze(
    state["applicant_data"]
)

 return state

def decision_node(state):

    state["decision"] = decision_agent.decide(
       state["profile"],
    state["risk"]
   )

    return state


def human_review_node(state):

 state["human_review"] = {

    "status": "Pending",

    "assigned_to": "Loan Officer",

    "review_reason":
        state["decision"]["reasoning"],

    "sla_hours": 24
}

 return state


def compliance_node(state):


   state["compliance"] = compliance_agent.execute(
      state["decision"],
    state["applicant_data"]
  )

   return state

# ------------------------------------------------

# Conditional Routing

# ------------------------------------------------

def route_decision(state):


 if (
    state["decision"]["decision"]
    == "Manual Review"
):

    return "HumanReview"

 return "Compliance"


# ------------------------------------------------

# LangGraph Construction

# ------------------------------------------------

workflow = StateGraph(LoanState)

workflow.add_node(
"ApplicantProfile",
applicant_node
)

workflow.add_node(
"FinancialRisk",
risk_node
)

workflow.add_node(
"LoanDecision",
decision_node
)

workflow.add_node(
"HumanReview",
human_review_node
)

workflow.add_node(
"Compliance",
compliance_node
)

workflow.set_entry_point(
"ApplicantProfile"
)

workflow.add_edge(
"ApplicantProfile",
"FinancialRisk"
)

workflow.add_edge(
"FinancialRisk",
"LoanDecision"
)

workflow.add_conditional_edges(
"LoanDecision",
route_decision,
{
"HumanReview": "HumanReview",
"Compliance": "Compliance"
}
)

workflow.add_edge(
"HumanReview",
"Compliance"
)

workflow.add_edge(
"Compliance",
END
)

graph = workflow.compile()

# ------------------------------------------------

# Main Process Function

# ------------------------------------------------

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

        "timestamp":
            datetime.utcnow().isoformat(),

        "applicant_id":
            data["applicant_id"],

        "profile":
            result["profile"],

        "risk":
            result["risk"],

        "decision":
            result["decision"],

        "compliance":
            result["compliance"]
    }

    if "human_review" in result:

        response["human_review"] = (
            result["human_review"]
        )

    return response