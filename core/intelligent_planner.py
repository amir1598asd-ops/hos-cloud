import json
from pathlib import Path



class IntelligentPlanner:


    def __init__(self):

        self.file = Path(
            "memory/workflow_scores.json"
        )


        if not self.file.exists():

            self.file.write_text(
                "{}",
                encoding="utf-8"
            )



    def load(self):

        return json.loads(
            self.file.read_text(
                encoding="utf-8"
            )
        )



    def recommend(
        self,
        task,
        available_agents
    ):


        memory=self.load()

        task_key=task.lower()


        selected=[]



        # use previous experience

        for key,value in memory.items():

            if key in task_key:

                ranked = sorted(
                    value.items(),
                    key=lambda x:x[1],
                    reverse=True
                )


                for agent,score in ranked:

                    if agent in available_agents:

                        selected.append(agent)



        # fallback

        if not selected:

            selected = available_agents[:3]



        return selected



    def learn(
        self,
        task,
        workflow,
        score
    ):


        data=self.load()


        key=task.lower()


        if key not in data:

            data[key]={}



        for agent in workflow:

            data[key][agent]=score



        self.file.write_text(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )