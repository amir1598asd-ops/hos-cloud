import requests



SERVER = "http://127.0.0.1:8000"



def send_task(goal):

    response = requests.post(

        SERVER + "/task",

        json={
            "goal": goal
        }

    )


    return response.json()



if __name__ == "__main__":


    result = send_task(
        "Build manga downloader"
    )


    print(result)