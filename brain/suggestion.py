class SuggestionEngine:


    def generate(
        self,
        risk
    ):


        suggestions=[]


        for item in risk["risks"]:


            if "High importance" in item:

                suggestions.append(
                    "Protect with tests before changes"
                )


            if "Many responsibilities" in item:

                suggestions.append(
                    "Consider refactoring"
                )


            if "High dependency" in item:

                suggestions.append(
                    "Review dependency structure"
                )


        if not suggestions:

            suggestions.append(
                "No immediate action"
            )


        return {

            "file":
                risk["file"],

            "suggestions":
                suggestions

        }