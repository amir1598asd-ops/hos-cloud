from datetime import datetime
import json
from pathlib import Path



class WorkflowExecutor:


    def __init__(self):

        self.file = Path(
            "memory/executions.json"
        )


        if not self.file.exists():

            self.file.write_text(
                "[]",
                encoding="utf-8"
            )



    def load(self):

        return json.loads(
            self.file.read_text(
                encoding="utf-8"
            )
        )



    def save(
        self,
        data
    ):

        self.file.write_text(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )



    def execute(
        self,
        task,
        agents
    ):


        results=[]


        context = task



        for agent in agents:


            result = agent.think(
                context
            )


            results.append(

                {
                    "agent":
                        agent.name,

                    "result":
                        result
                }

            )


            context = (
                str(result)
            )



        record={

            "time":
                datetime.now().isoformat(),

            "task":
                task,

            "results":
                results,

            "status":
                "completed"

        }


        history=self.load()

        history.append(record)

        self.save(history)


        return record