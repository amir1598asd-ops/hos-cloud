from datetime import datetime


class HOSRuntime:

    def __init__(self):
        self.agents = {}
        self.history = []


    def register_agent(self, agent):

        self.agents[agent.name] = agent


    def list_agents(self):

        return list(self.agents.keys())


    def execute(self, task):

        result = {
            "time": datetime.now().isoformat(),
            "task": task,
            "agents": []
        }


        for name, agent in self.agents.items():

            output = agent.think(task)

            result["agents"].append(
                {
                    "agent": name,
                    "output": output
                }
            )


        self.history.append(result)

        return result