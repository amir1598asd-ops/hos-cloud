from fastapi import FastAPI

from hos_server.runtime_service import RuntimeService


app = FastAPI(
    title="HOS Cloud"
)


runtime = RuntimeService()



@app.get("/")
def home():

    return {
        "system":
            "HOS Cloud",

        "status":
            "online"
    }



@app.post("/task")
def create_task(data:dict):

    return runtime.run_task(
        data["goal"]
    )