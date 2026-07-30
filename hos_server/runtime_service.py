from datetime import datetime


class RuntimeService:


    def __init__(self):

        self.tasks = []


    def run_task(self, task):

        result = {

            "time":
                datetime.now().isoformat(),

            "task":
                task,

            "status":
                "completed",

            "result":
                f"HOS processed: {task}"

        }


        self.tasks.append(result)


        return result