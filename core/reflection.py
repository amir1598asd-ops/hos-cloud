import json
from pathlib import Path
from datetime import datetime



class ReflectionEngine:


    def __init__(self):

        self.file = Path(
            "memory/reflections.json"
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



    def reflect(
        self,
        decision,
        evaluation
    ):


        ranking = evaluation["ranking"]


        best = ranking[0]["agent"]


        reflection = {

            "time":
                datetime.now().isoformat(),


            "task":
                decision["task"],


            "decision":
                decision["decision"],


            "best_agent":
                best,


            "lesson":

                f"{best} provided the strongest contribution",



            "future_rule":

                "Use successful agent strategies in similar tasks"

        }


        history = self.load()


        history.append(
            reflection
        )


        self.save(
            history
        )


        return reflection