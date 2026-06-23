from fastmcp import FastMCP

app = FastMCP("DecisionSynthesis")


@app.tool()
def synthesize_decision(profile, risk):

    if profile["profile_score"] > 70 and risk["risk"] == "Low":
        return "Approved"

    if risk["risk"] == "High":
        return "Rejected"

    return "Manual Review"


if __name__ == "__main__":
    app.run()