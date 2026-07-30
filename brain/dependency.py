import ast


class DependencyAnalyzer:


    def analyze(self, file):

        try:

            text = open(
                file,
                encoding="utf-8"
            ).read()


            tree = ast.parse(text)


            imports = []


            for node in ast.walk(tree):

                if isinstance(
                    node,
                    ast.Import
                ):

                    for item in node.names:

                        imports.append(
                            item.name
                        )


                if isinstance(
                    node,
                    ast.ImportFrom
                ):

                    if node.module:

                        imports.append(
                            node.module
                        )


            return {

                "file": file,

                "imports": imports,

                "dependency_count":
                    len(imports)

            }


        except Exception as e:

            return {

                "file": file,

                "error": str(e)

            }