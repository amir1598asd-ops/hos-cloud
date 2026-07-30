class PlannerBrain:


    def plan(
        self,
        task
    ):


        task=task.lower()


        nodes=[]



        if "code" in task or "build" in task:

            nodes=[
                "Researcher",
                "Critic",
                "Coder",
                "Tester",
                "Memory"
            ]


        elif "idea" in task:

            nodes=[
                "Researcher",
                "Debate",
                "Critic",
                "Memory"
            ]


        else:

            nodes=[
                "Researcher",
                "Council",
                "Memory"
            ]



        return nodes