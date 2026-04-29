@app.get("/tasks")
def get_tasks():
    return {"tasks": ["Task 1", "Task 2"]}
