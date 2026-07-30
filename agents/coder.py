from .base_agent import BaseAgent



class CoderAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "Coder",
            "Create and improve code"
        )



    def think(
        self,
        problem
    ):

        return {

            "agent":
                self.name,

            "role":
                "Developer",

            "idea":
                [
                    "Analyze current implementation",
                    "Design cleaner solution",
                    "Create possible code change"
                ]

        }