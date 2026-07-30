class RiskAnalyzer:


    def analyze(
        self,
        architecture,
        priority
    ):

        risks = []


        if priority["score"] > 30:

            risks.append(
                "High importance component"
            )


        if len(
            architecture["functions"]
        ) > 8:

            risks.append(
                "Many responsibilities"
            )


        if len(
            architecture["imports"]
        ) > 5:

            risks.append(
                "High dependency"
            )


        if not risks:

            risks.append(
                "Low risk"
            )


        return {

            "file":
                architecture["file"],

            "risks":
                risks

        }