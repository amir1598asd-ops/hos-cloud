from pathlib import Path


class AgentCodeGenerator:


    def generate(
        self,
        name,
        role,
        skills
    ):


        class_name = (
            name + "Agent"
        )


        code = f"""
from .base_agent import BaseAgent


class {class_name}(BaseAgent):


    def __init__(self):

        super().__init__(
            "{name}",
            "{role}"
        )


    def think(
        self,
        problem
    ):

        return {{
            "agent":
                self.name,

            "role":
                "{role}",

            "skills":
                {skills},

            "analysis":
                f"{{self.name}} analyzing {{problem}}"
        }}
"""


        file = Path(
            f"agents/{name.lower()}.py"
        )


        file.write_text(
            code.strip(),
            encoding="utf-8"
        )


        return str(file)