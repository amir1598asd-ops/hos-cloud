class AgentDetector:


    def analyze(
        self,
        task,
        existing
    ):


        required=[]


        task=task.lower()


        if "manga" in task or "image" in task:

            required.append(
                {
                "name":"ImageParser",
                "role":"Extract images from websites",
                "skills":[
                    "HTML parsing",
                    "image detection"
                ]
                }
            )


        if "test" in task or "code" in task:

            required.append(
                {
                "name":"Tester",
                "role":"Software testing",
                "skills":[
                    "bug detection",
                    "validation"
                ]
                }
            )


        missing=[]


        for agent in required:

            if agent["name"] not in existing:

                missing.append(agent)


        return missing