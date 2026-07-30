from .base_agent import BaseAgent



class CriticAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "Critic",
            "Find problems and weaknesses"
        )



    def think(
        self,
        problem
    ):

        return {

            "agent":
                self.name,

            "role":
                "Reviewer",

            "idea":
                [
                    "Find possible failures",
                    "Check hidden risks",
                    "Challenge assumptions"
                ]

        }