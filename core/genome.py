import json
from pathlib import Path
from datetime import datetime


class GenomeManager:


    def __init__(self):

        self.file = Path(
            "memory/agent_genomes.json"
        )


        if not self.file.exists():

            self.file.write_text(
                json.dumps(
                    {
                        "Coder":{
                            "creativity":70,
                            "accuracy":70,
                            "speed":70,
                            "wins":0,
                            "failures":0
                        },

                        "Critic":{
                            "bug_detection":80,
                            "strictness":70,
                            "wins":0,
                            "failures":0
                        },

                        "Researcher":{
                            "innovation":80,
                            "knowledge":70,
                            "wins":0,
                            "failures":0
                        }
                    },
                    indent=2
                ),
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
                indent=2
            ),
            encoding="utf-8"
        )



    def reward(self, agent, value):

        data=self.load()


        if agent in data:

            data[agent]["wins"] += 1


            for key in data[agent]:

                if isinstance(
                    data[agent][key],
                    int
                ) and key not in [
                    "wins",
                    "failures"
                ]:

                    data[agent][key]+=value



        self.save(data)



    def punish(self, agent):

        data=self.load()


        if agent in data:

            data[agent]["failures"] += 1



        self.save(data)



    def profile(self,agent):

        return self.load().get(
            agent,
            {}
        )