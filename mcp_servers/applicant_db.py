from fastmcp import FastMCP

app = FastMCP("ApplicantDB")


@app.tool()
def get_applicant_profile(applicant_id: str):

    return {
        "applicant_id": applicant_id,
        "existing_customer": True,
        "past_defaults": 0,
        "loan_history": "Good"
    }


if __name__ == "__main__":
    app.run()