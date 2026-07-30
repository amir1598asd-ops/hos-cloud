import json


class Insight:


    def create(self, results):

        results.sort(
            key=lambda x:x["score"],
            reverse=True
        )


        return {

            "most_important_files":
                results[:5],

            "recommendation":
                "Analyze highest priority files first"

        }


    def save(self, data):

        with open(
            "memory/brain_insight.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=2,
                ensure_ascii=False
            )