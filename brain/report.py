import json
from datetime import datetime


class Report:


    def create(self, scan, analysis):

        return {

            "time":
                datetime.now().isoformat(),

            "project":
                scan["project"],

            "python_files":
                scan["python_files"],

            "analysis":
                analysis

        }


    def save(self, data):

        with open(
            "memory/project_report.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=2,
                ensure_ascii=False
            )