import json
from pathlib import Path
from datetime import datetime



class AgentFactory:


    def __init__(self):

        self.file = Path(
            "memory/created_agents.json"
        )


        if not self.file.exists():

            self.file.write_text(
                "[]",
                encoding="utf-8"
            )



    def create_agent(
        self,
        name,
        role,
        skills
    ):


        agent={

            "time":
                datetime.now().isoformat(),

            "name":
                name,

            "role":
                role,

            "skills":
                skills,

            "experience":
                0,

            "score":
                0

        }



        data=json.loads(
            self.file.read_text(
                encoding="utf-8"
            )
        )


        data.append(
            agent
        )


        self.file.write_text(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )


        return agent