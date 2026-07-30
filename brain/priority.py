class PriorityBrain:


    def calculate(
        self,
        complexity,
        dependency
    ):


        score = 0


        score += complexity.get(
            "function_count",
            0
        ) * 5


        score += dependency.get(
            "dependency_count",
            0
        ) * 3


        if score > 50:

            level = "critical"

        elif score > 20:

            level = "important"

        else:

            level = "normal"


        return {

            "file":
                complexity["file"],

            "score":
                score,

            "priority":
                level

        }