class HOSAgent:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def run(self, task):

        return {
            "role": self.role,
            "message":
                f"{self.name} processing {task}"
        }