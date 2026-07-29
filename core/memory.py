import json
from pathlib import Path
from datetime import datetime


class HOSMemory:

    def __init__(self):
        self.path = Path("memory")
        self.path.mkdir(exist_ok=True)

        self.knowledge_file = self.path / "knowledge.json"
        self.experience_file = self.path / "experiences.json"
        self.genome_file = self.path / "genome.json"

        self._init_files()


    def _init_files(self):

        defaults = {
            self.knowledge_file: {},
            self.experience_file: [],
            self.genome_file: {
                "version": "0.1",
                "learning_rate": 0.1,
                "mutation_rate": 0.05
            }
        }

        for file, data in defaults.items():
            if not file.exists():
                file.write_text(
                    json.dumps(data, indent=2),
                    encoding="utf-8"
                )


    def add_experience(self, task, result, lesson):

        data = json.loads(
            self.experience_file.read_text(encoding="utf-8")
        )

        data.append({
            "time": datetime.now().isoformat(),
            "task": task,
            "result": result,
            "lesson": lesson
        })

        self.experience_file.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )


    def remember(self, key, value):

        data = json.loads(
            self.knowledge_file.read_text(encoding="utf-8")
        )

        data[key] = value

        self.knowledge_file.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )


    def recall(self, key):

        data = json.loads(
            self.knowledge_file.read_text(encoding="utf-8")
        )

        return data.get(key)


    def get_history(self):

        return json.loads(
            self.experience_file.read_text(encoding="utf-8")
        )


if __name__ == "__main__":

    memory = HOSMemory()

    memory.add_experience(
        "test",
        "success",
        "memory system works"
    )

    memory.remember(
        "first_lesson",
        "HOS can remember"
    )

    print("Memory Brain online")
