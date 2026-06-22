from langgraph.graph import StateGraph, END

from agents.applicant_agent import ApplicantAgent
from agents.financial_agent import FinancialRiskAgent
from agents.decision_agent import DecisionAgent
from agents.compliance_agent import ComplianceAgent

from orchestrator.state import LoanState
from database.audit_service import save_audit

applicant_agent = ApplicantAgent()
risk_agent = FinancialRiskAgent()
decision_agent = DecisionAgent()
compliance_agent = ComplianceAgent()


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


def compliance_node(state):

    state["compliance"] = compliance_agent.execute(
        state["decision"]
    )

    return state


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

workflow.add_edge(
    "LoanDecision",
    "Compliance"
)

workflow.add_edge(
    "Compliance",
    END
)

graph = workflow.compile()


def process_loan(data):

    result = graph.invoke(
        {
            "applicant_data": data
        }
    )

    save_audit(
        applicant_id=data["applicant_id"],
        decision=result["decision"]["decision"],
        confidence=result["decision"]["confidence"],
        reasoning=result["decision"]["reasoning"]
    )

    return {
        "profile": result["profile"],
        "risk": result["risk"],
        "decision": result["decision"],
        "compliance": result["compliance"]
    }