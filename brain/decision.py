class DecisionBrain:


    def choose(
        self,
        discussion
    ):


        opinions = discussion["opinions"]


        if not opinions:

            return {
                "decision":
                    "No ideas"
            }


        return {

            "decision":
                "Evaluate all proposals",

            "participants":
                [
                    x["agent"]
                    for x in opinions
                ],

            "next_step":
                "Send best idea to Coder"

        }