import importlib
from pathlib import Path


class PluginManager:


    def __init__(self, runtime):

        self.runtime = runtime



    def load_all(self):

        folder = Path("hos_plugins")


        for item in folder.iterdir():

            if item.is_dir() and item.name != "__pycache__":

                try:

                    module = importlib.import_module(
                        f"hos_plugins.{item.name}"
                    )


                    for name in dir(module):

                        obj = getattr(
                            module,
                            name
                        )


                        if isinstance(obj, type):

                            if name.endswith("Plugin"):

                                agent = obj()

                                self.runtime.register_agent(
                                    agent
                                )

                                print(
                                    "Loaded:",
                                    agent.name
                                )


                except Exception as e:

                    print(
                        "Plugin error:",
                        item.name,
                        e
                    )