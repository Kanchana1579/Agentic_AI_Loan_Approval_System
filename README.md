# Agentic_AI_Loan_Approval_System

## Overview

The Agentic AI Loan Approval System is a multi-agent AI application that automates loan application analysis and approval decisions.

The system uses specialized AI agents to evaluate applicant information, assess financial risk, perform compliance checks, and generate a final loan approval decision.

## Features

* Multi-Agent Architecture
* Applicant Profile Analysis
* Financial Risk Assessment
* Debt-to-Income (DTI) Calculation
* Compliance Validation
* Automated Loan Decisioning
* FastAPI Backend
* Streamlit Frontend
* LangGraph Workflow Orchestration
* Anthropic Claude Integration

## Architecture

### Agents

1. Applicant Agent

   * Validates applicant details
   * Evaluates applicant profile

2. Financial Risk Agent

   * Calculates DTI Ratio
   * Assesses liabilities and income
   * Generates risk score

3. Compliance Agent

   * Performs compliance checks
   * Validates business rules

4. Decision Agent

   * Generates final decision
   * Provides approval/rejection reasoning

## Project Structure

agentic-loan-approval/

├── agents/

├── backend/

├── database/

├── mcp_servers/

├── orchestrator/

├── ui/

├── requirements.txt

└── create_db.py

## Technology Stack

* Python
* FastAPI
* Streamlit
* LangGraph
* Anthropic Claude
* SQLite
* Pydantic

## Installation

### Clone Repository

git clone https://github.com/Kanchana1579/Agentic_AI_Loan_Approval_System.git

cd Agentic_AI_Loan_Approval_System

### Create Virtual Environment

python -m venv venv

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create a .env file:

ANTHROPIC_API_KEY=your_api_key

## Run Application

### Start Backend

uvicorn backend.main:app --reload

### Start Streamlit UI

streamlit run ui/streamlit_app.py

## Sample Loan Approval Logic

Approval Criteria:

* Credit Score ≥ 700
* DTI ≤ 40%
* Monthly Income ≥ ₹40,000
* Compliance Status = PASSED

## API Endpoint

POST /loan/evaluate

### Sample Request

{
"applicant_id": "APPL-001",
"age": 32,
"income": 100000,
"liabilities": 20000,
"credit_score": 780
}

### Sample Response

{
"decision": "APPROVED",
"risk_level": "LOW",
"dti_ratio": 20
}

## Future Enhancements

* RAG-based document verification
* Vector Database Integration
* Human-in-the-loop approval workflow
* Credit Bureau API Integration
* Deployment on AWS/Azure

## Author

Kanchana Singh
Data Engineer | Azure | Databricks | PySpark | AI Applications
