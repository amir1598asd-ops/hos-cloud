import ast


class ArchitectureAnalyzer:


    def analyze(self, file):

        result = {

            "file": file,

            "classes": [],

            "functions": [],

            "imports": []

        }


        try:

            text = open(
                file,
                encoding="utf-8"
            ).read()


            tree = ast.parse(text)


            for node in ast.walk(tree):

                if isinstance(
                    node,
                    ast.ClassDef
                ):

                    result["classes"].append(
                        node.name
                    )


                if isinstance(
                    node,
                    ast.FunctionDef
                ):

                    result["functions"].append(
                        node.name
                    )


                if isinstance(
                    node,
                    ast.Import
                ):

                    for item in node.names:
                        result["imports"].append(
                            item.name
                        )


                if isinstance(
                    node,
                    ast.ImportFrom
                ):

                    if node.module:
                        result["imports"].append(
                            node.module
                        )


        except Exception as e:

            result["error"] = str(e)


        return result