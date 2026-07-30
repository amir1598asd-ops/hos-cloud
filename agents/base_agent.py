class BaseAgent:


    def __init__(
        self,
        name,
        goal
    ):

        self.name = name

        self.goal = goal

        self.experience = []

        self.score = 0



    def think(
        self,
        problem
    ):

        return {

            "agent":
                self.name,

            "thinking":
                f"{self.name} analyzing {problem}"

        }



    def learn(
        self,
        lesson
    ):

        self.experience.append(
            lesson
        )



    def reward(
        self,
        value
    ):

        self.score += value



    def report(self):

        return {

            "name":
                self.name,

            "goal":
                self.goal,

            "experience":
                len(self.experience),

            "score":
                self.score

        }