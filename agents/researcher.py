from .base_agent import BaseAgent



class ResearcherAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "Researcher",
            "Find new solutions and knowledge"
        )



    def think(
        self,
        problem
    ):

        return {

            "agent":
                self.name,

            "role":
                "Researcher",

            "idea":
                [
                    "Compare known methods",
                    "Find better approaches",
                    "Suggest improvements"
                ]

        }