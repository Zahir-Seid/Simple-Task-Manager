from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

DATA_FILE = "tasks.json"

# Task model
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

class TaskCreate(BaseModel):
    title: str

# Utility functions
def read_tasks() -> List[Task]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return [Task(**task) for task in json.load(f)]

def write_tasks(tasks: List[Task]):
    with open(DATA_FILE, "w") as f:
        json.dump([task.dict() for task in tasks], f, indent=2)

# Root route (optional "API is running" page)
@app.get("/")
def read_root():
    return {"message": "API is running."}

# GET all tasks
@app.get("/api/tasks", response_model=List[Task])
def get_tasks():
    return read_tasks()

# POST a new task
@app.post("/api/tasks", response_model=Task)
def add_task(task: TaskCreate):
    tasks = read_tasks()
    new_id = max([t.id for t in tasks], default=0) + 1
    new_task = Task(id=new_id, title=task.title)
    tasks.append(new_task)
    write_tasks(tasks)
    return new_task

# PUT to mark task as completed
@app.put("/api/tasks/{task_id}", response_model=Task)
def complete_task(task_id: int):
    tasks = read_tasks()
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            write_tasks(tasks)
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# DELETE a task
@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = read_tasks()
    updated_tasks = [task for task in tasks if task.id != task_id]
    if len(updated_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    write_tasks(updated_tasks)
    return {"message": f"Task {task_id} deleted successfully"}
