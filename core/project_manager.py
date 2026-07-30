import json
from pathlib import Path
from datetime import datetime



class ProjectManager:


    def __init__(
        self,
        planner,
        registry
    ):

        self.planner = planner
        self.registry = registry

        self.file = Path(
            "memory/projects.json"
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



    def create_project(
        self,
        goal
    ):


        agents = list(
            self.registry.list_agents().keys()
        )


        selected = self.planner.recommend(
            goal,
            agents
        )


        project = {

            "time":
                datetime.now().isoformat(),

            "goal":
                goal,

            "agents":
                selected,

            "status":
                "planned"
        }



        history=self.load()

        history.append(project)

        self.save(history)



        return project