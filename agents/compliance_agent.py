from datetime import datetime

class ComplianceAgent:

    def execute(self,decision):

        return {
            "timestamp":str(datetime.now()),
            "action":decision["decision"],
            "notification":"Sent"
        }