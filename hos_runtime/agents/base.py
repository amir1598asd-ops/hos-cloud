class RuntimeAgent:


    def __init__(
        self,
        name,
        role
    ):

        self.name = name
        self.role = role


    def think(self, task):

        return {
            "role": self.role,
            "message":
                f"{self.name} processing {task}"
        }