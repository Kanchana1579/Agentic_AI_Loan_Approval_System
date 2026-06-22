from fastmcp import FastMCP

app = FastMCP("Notification")


@app.tool()
def send_notification(applicant_id, decision):

    return {
        "status": "Sent",
        "applicant_id": applicant_id,
        "decision": decision
    }


if __name__ == "__main__":
    app.run()