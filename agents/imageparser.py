from .base_agent import BaseAgent


class ImageParserAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "ImageParser",
            "Extract images from websites"
        )


    def think(
        self,
        problem
    ):

        return {
            "agent":
                self.name,

            "role":
                "Extract images from websites",

            "skills":
                ['HTML parsing', 'image detection'],

            "analysis":
                f"{self.name} analyzing {problem}"
        }