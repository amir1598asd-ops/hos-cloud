from pathlib import Path
import importlib


class PluginLoader:

    def __init__(self, folder="hos_plugins"):
        self.folder = Path(folder)


    def discover(self):

        plugins = []

        if not self.folder.exists():
            return plugins


        for item in self.folder.iterdir():

            if item.is_dir():

                plugins.append(
                    item.name
                )

        return plugins