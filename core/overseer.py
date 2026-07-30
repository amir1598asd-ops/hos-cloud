from agents.coder import CoderAgent
from agents.critic import CriticAgent
from agents.researcher import ResearcherAgent


class Overseer:

    def __init__(self):

        self.agents = [
            CoderAgent(),
            CriticAgent(),
            ResearcherAgent()
        ]


    def assign_task(self, task):

        results = []

        for agent in self.agents:

            result = agent.think(task)

            agent.learn(
                f"Worked on: {task}"
            )

            results.append({
                "agent": agent.name,
                "result": result
            })

        return results


    def status(self):

        return [
            agent.report()
            for agent in self.agents
        ]