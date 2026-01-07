from fastapi import FastAPI, status, HTTPException

app = FastAPI()

tasks_db = {0: "Study FastAPI", 1: "I like FastAPI"}

@app.get("/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def read_task(task_id : int) -> str:
    try:
        return tasks_db[task_id]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


from fastapi import FastAPI, Body, status

app = FastAPI()

reminders_db = {}

@app.post("/reminders", status_code=status.HTTP_201_CREATED)
async def create_notion (message : str = Body(...)) -> str:
    current_index = max(reminders_db) + 1 if reminders_db else 0
    reminders_db[current_index] = message
    return "Message created!"