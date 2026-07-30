import json
from pathlib import Path
from datetime import datetime



class WorkflowGraph:


    def __init__(self):

        self.file = Path(
            "memory/workflows.json"
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



    def save(self,data):

        self.file.write_text(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )



    def create(
        self,
        task,
        nodes
    ):


        workflow={

            "time":
                datetime.now().isoformat(),

            "task":
                task,


            "nodes":
                nodes,


            "connections":[]

        }



        for i in range(
            len(nodes)-1
        ):

            workflow["connections"].append({

                "from":
                    nodes[i],

                "to":
                    nodes[i+1]

            })



        history=self.load()


        history.append(
            workflow
        )


        self.save(
            history
        )


        return workflow