from datetime import datetime


class HOSRuntime:


    def __init__(self):

        self.agents = {}



    def register_agent(self, agent):

        self.agents[agent.name] = agent



    def list_agents(self):

        return list(
            self.agents.keys()
        )



    def execute(self, task):

        results=[]


        for name, agent in self.agents.items():

            results.append(
                {
                    "agent": name,
                    "output": agent.run(task)
                }
            )


        return {
            "time": datetime.now().isoformat(),
            "task": task,
            "results": results
        }