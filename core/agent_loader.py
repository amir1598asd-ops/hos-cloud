import importlib
from pathlib import Path



class AgentLoader:


    def __init__(self):

        self.loaded = {}



    def load_agent(
        self,
        name
    ):


        module_name = (
            "agents."
            +
            name.lower()
        )


        class_name = (
            name
            +
            "Agent"
        )


        module = importlib.import_module(
            module_name
        )


        agent_class = getattr(
            module,
            class_name
        )


        agent = agent_class()


        self.loaded[name]=agent


        return agent



    def load_all(
        self,
        registry
    ):


        agents=[]


        for name in registry.list_agents():

            try:

                agents.append(
                    self.load_agent(name)
                )


            except Exception as e:

                print(
                    "Failed loading",
                    name,
                    e
                )


        return agents