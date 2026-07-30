import ast


class CodeAnalyzer:


    def analyze_file(self, file):

        try:

            text = open(
                file,
                encoding="utf-8"
            ).read()


            tree = ast.parse(text)


            functions = []

            classes = []


            for node in ast.walk(tree):

                if isinstance(
                    node,
                    ast.FunctionDef
                ):
                    functions.append(
                        node.name
                    )


                if isinstance(
                    node,
                    ast.ClassDef
                ):
                    classes.append(
                        node.name
                    )


            return {

                "file": file,

                "functions": functions,

                "classes": classes,

                "function_count":
                    len(functions),

                "class_count":
                    len(classes)

            }


        except Exception as e:

            return {

                "file": file,

                "error": str(e)

            }