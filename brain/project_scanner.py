from pathlib import Path


class ProjectScanner:

    def scan(self, path):

        root = Path(path)

        files = list(root.rglob("*.py"))

        return {

            "project": str(root),

            "python_files": len(files),

            "files": [
                str(f)
                for f in files
            ]

        }