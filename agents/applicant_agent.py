class ApplicantAgent:

    def analyze(self,data):

        score = 0

        if data["annual_income"] > 1000000:
            score += 40

        if data["employment_type"] == "Permanent":
            score += 30

        if data["credit_score"] > 700:
            score += 30

        return {
            "profile_score":score,
            "employment_risk":"Low"
        }