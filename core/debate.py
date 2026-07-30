import json
from pathlib import Path
from datetime import datetime



class DebateEngine:


    def __init__(self):

        self.file = Path(
            "memory/debates.json"
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



    def debate(
        self,
        task,
        agents
    ):


        session={

            "time":
                datetime.now().isoformat(),

            "task":
                task,

            "rounds":[]

        }



        # Round 1: independent thinking

        ideas=[]


        for agent in agents:

            ideas.append({

                "agent":
                    agent.name,

                "idea":
                    agent.think(task)

            })



        session["rounds"].append({

            "name":
                "independent thinking",

            "messages":
                ideas

        })



        # Shared memory

        shared_context = json.dumps(
            ideas,
            ensure_ascii=False
        )



        # Round 2: agents see each other

        improved=[]


        for agent in agents:


            improved.append({

                "agent":
                    agent.name,


                "response":

                    {
                    "based_on":
                        shared_context,

                    "new_thought":

                        f"{agent.name} improved its idea after reviewing others"
                    }

            })



        session["rounds"].append({

            "name":
                "collaborative improvement",

            "messages":
                improved

        })



        history=self.load()

        history.append(
            session
        )

        self.save(
            history
        )


        return session