from fastmcp import FastMCP

app = FastMCP("RiskRules")


@app.tool()
def get_risk_rules():

    return {
        "minimum_credit_score": 650,
        "maximum_dti": 0.50,
        "maximum_loan_ratio": 5
    }


if __name__ == "__main__":
    app.run()