# task_api.py
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import uuid4
from datetime import datetime

app = FastAPI(title="Task Manager API")

# -------------------------
# 1) Models
# -------------------------
class TaskBase(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field("", max_length=1000)
    completed: Optional[bool] = False

class TaskCreate(TaskBase):
    # For create, title must be present - override
    title: str = Field(..., min_length=1, max_length=200)


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    
class Task(TaskBase):
    id: str
    created_at: datetime


# -------------------------
# 2) In-memory store + helpers
# -------------------------
_tasks: List[Task] = []

def _find_index(task_id: str) -> Optional[int]:
    for i, t in enumerate(_tasks):
        if t.id == task_id:
            return i
    return None

# -------------------------
# 3) Endpoints (CRUD)
# -------------------------

@app.post("/tasks/", status_code=201, response_model=Task)
def create_task(task_in: TaskCreate):
    """Create new task"""
    new_task = Task(
        id=str(uuid4()),
        title=task_in.title,
        description=task_in.description or "",
        completed=task_in.completed if task_in.completed is not None else False,
        created_at=datetime.utcnow()
    )
    _tasks.append(new_task)
    return new_task


@app.get("/tasks/", response_model=List[Task])
def list_tasks():
    """📋 View all tasks"""
    return _tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    """🔍 Get a single task by ID"""
    idx = _find_index(task_id)
    if idx is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return _tasks[idx]


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task_in: TaskUpdate):
    """Update (replace) an existing task"""
    idx = _find_index(task_id)
    if idx is None:
        raise HTTPException(status_code=404, detail="Task not found")

    old_task = _tasks[idx]
       
    updated_task = Task(
        id=old_task.id,
        title=task_in.title if task_in.title is not None else old_task.title,
        description=task_in.description if task_in.description is not None else old_task.description,
        completed=task_in.completed if task_in.completed is not None else old_task.completed,
        created_at=old_task.created_at
    )

    _tasks[idx] = updated_task
    return updated_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    idx = _find_index(task_id)
    if idx is None:
        raise HTTPException(status_code=404, detail="Task not found")
    removed = _tasks.pop(idx)
    return {"status": "success", "id": removed.id, "message": "Deleted"}

