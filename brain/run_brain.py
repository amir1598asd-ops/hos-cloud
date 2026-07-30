import sys
import json

from brain.project_scanner import ProjectScanner
from brain.complexity import ComplexityAnalyzer
from brain.dependency import DependencyAnalyzer
from brain.priority import PriorityBrain
from brain.architecture import ArchitectureAnalyzer
from brain.risk import RiskAnalyzer
from brain.suggestion import SuggestionEngine



def main():

    if len(sys.argv)<2:

        print(
            "Usage: python -m brain.run_brain PROJECT"
        )

        return


    project=sys.argv[1]


    scanner=ProjectScanner()
    complexity=ComplexityAnalyzer()
    dependency=DependencyAnalyzer()
    priority=PriorityBrain()
    architecture=ArchitectureAnalyzer()
    risk=RiskAnalyzer()
    suggestion=SuggestionEngine()


    scan=scanner.scan(project)


    results=[]


    for file in scan["files"]:


        c=complexity.analyze(file)

        d=dependency.analyze(file)


        p=priority.calculate(
            c,
            d
        )


        a=architecture.analyze(file)


        r=risk.analyze(
            a,
            p
        )


        s=suggestion.generate(r)


        results.append({

            "priority":p,

            "architecture":a,

            "risk":r,

            "suggestion":s

        })


    results.sort(
        key=lambda x:
        x["priority"]["score"],
        reverse=True
    )


    output={

        "project":
            project,

        "files_analyzed":
            len(results),

        "architect_analysis":
            results[:10]

    }


    with open(
        "memory/architect_insight.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            output,
            f,
            indent=2,
            ensure_ascii=False
        )


    print(
        "HOS Brain v0.3 completed"
    )

    print(
        "Architect insight saved:"
        " memory/architect_insight.json"
    )


if __name__=="__main__":

    main()