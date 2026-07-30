import json
from pathlib import Path
from datetime import datetime



class AgentRegistry:


    def __init__(self):

        self.file = Path(
            "memory/agent_registry.json"
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



    def register(
        self,
        name,
        role,
        skills
    ):


        data=self.load()


        data[name]={

            "created":
                datetime.now().isoformat(),

            "role":
                role,

            "skills":
                skills,

            "status":
                "active"

        }


        self.file.write_text(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )


        return data[name]



    def exists(
        self,
        name
    ):

        return name in self.load()



    def list_agents(self):

        return self.load()