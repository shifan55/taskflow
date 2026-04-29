from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "TaskFlow API is running"}
@app.get("/tasks")
def get_tasks():
    return {"tasks": ["Task 1", "Task 2"]}
