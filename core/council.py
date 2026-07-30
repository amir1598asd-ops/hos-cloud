import json
from pathlib import Path
from datetime import datetime

from core.decision import DecisionBrain
from core.evaluator import Evaluator
from core.reflection import ReflectionEngine



class Council:


    def __init__(self):


        self.memory_file = Path(
            "memory/council.json"
        )


        self.decision = DecisionBrain()


        self.evaluator = Evaluator()


        self.reflection = ReflectionEngine()



        if not self.memory_file.exists():

            self.memory_file.write_text(
                '{"sessions":[],"scores":{}}',
                encoding="utf-8"
            )



    def load(self):

        return json.loads(
            self.memory_file.read_text(
                encoding="utf-8"
            )
        )



    def save(self,data):

        self.memory_file.write_text(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )



    def discuss(
        self,
        task,
        agents
    ):


        result = {

            "time":
                datetime.now().isoformat(),


            "task":
                task,


            "opinions":[]

        }



        for agent in agents:


            opinion = agent.think(task)


            result["opinions"].append({

                "agent":
                    agent.name,


                "goal":
                    agent.goal,


                "opinion":
                    opinion

            })



        evaluation = self.evaluator.evaluate(
            result["opinions"]
        )



        result["evaluation"] = evaluation



        decision = self.decision.decide(
            result
        )



        result["decision"] = decision



        result["reflection"] = self.reflection.reflect(
            decision,
            evaluation
        )



        memory = self.load()


        memory["sessions"].append(
            result
        )


        self.save(
            memory
        )


        return result