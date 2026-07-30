import json
from pathlib import Path
from datetime import datetime


class Evaluator:


    def __init__(self):

        self.file = Path(
            "memory/agent_scores.json"
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


    def save(self,data):

        self.file.write_text(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )


    def evaluate(
        self,
        opinions
    ):

        scores = self.load()

        result = []


        for opinion in opinions:

            agent = opinion["agent"]

            idea = opinion["opinion"]


            score = 0


            # basic intelligence scoring
            if "idea" in idea:

                score += len(
                    idea["idea"]
                )


            if agent == "Critic":

                score += 2


            if agent == "Researcher":

                score += 3


            if agent == "Coder":

                score += 2



            if agent not in scores:

                scores[agent] = {
                    "total":0,
                    "runs":0
                }


            scores[agent]["total"] += score

            scores[agent]["runs"] += 1


            result.append({

                "agent":
                    agent,

                "score":
                    score

            })


        self.save(scores)


        return {

            "time":
                datetime.now().isoformat(),

            "ranking":
                sorted(
                    result,
                    key=lambda x:x["score"],
                    reverse=True
                )

        }