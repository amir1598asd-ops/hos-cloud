import ast


class ComplexityAnalyzer:


    def analyze(self, file):

        try:

            text = open(
                file,
                encoding="utf-8"
            ).read()


            tree = ast.parse(text)


            functions = []


            for node in ast.walk(tree):

                if isinstance(
                    node,
                    ast.FunctionDef
                ):

                    functions.append({

                        "name": node.name,

                        "lines":
                            node.end_lineno - node.lineno + 1

                    })


            score = len(functions)

            if score > 10:

                level = "high"

            elif score > 4:

                level = "medium"

            else:

                level = "low"


            return {

                "file": file,

                "function_count": len(functions),

                "complexity": level,

                "functions": functions

            }


        except Exception as e:

            return {

                "file": file,

                "error": str(e)

            }