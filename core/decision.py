import json
from pathlib import Path
from datetime import datetime


class DecisionBrain:


    def __init__(self):

        self.file = Path(
            "memory/decision_history.json"
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


    def save(self, data):

        self.file.write_text(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )


    def decide(
        self,
        discussion
    ):


        opinions = discussion["opinions"]


        decision = {

            "time":
                datetime.now().isoformat(),

            "task":
                discussion["task"],

            "opinions":
                opinions,

            "decision":
                "",

            "reason":
                ""

        }


        agents = [
            x["agent"]
            for x in opinions
        ]


        if "Coder" in agents:

            decision["decision"] = (
                "Create improvement proposal"
            )

            decision["reason"] = (
                "Coder can transform ideas into implementation"
            )

        else:

            decision["decision"] = (
                "Need more analysis"
            )

            decision["reason"] = (
                "Not enough agents participated"
            )


        history = self.load()

        history.append(
            decision
        )

        self.save(
            history
        )


        return decision