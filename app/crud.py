from sqlalchemy.orm import Session
from .models import Task, StatusEnum
from .schemas import TaskCreate, TaskUpdate
from typing import List, Optional
from datetime import date

def create_task(db: Session, task_data: TaskCreate) -> Task:
    task = Task(**task_data.dict(exclude_unset=True))
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task(db: Session, task_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(
    db: Session,
    status: Optional[StatusEnum] = None,
    due_date: Optional[date] = None
) -> List[Task]:
    query = db.query(Task)
    if status is not None:
        query = query.filter(Task.status == status)
    if due_date is not None:
        query = query.filter(Task.due_date == due_date)
    return query.all()

def update_task(db: Session, task_id: int, task_data: TaskUpdate) -> Optional[Task]:
    task = get_task(db, task_id)
    if not task:
        return None
    update_data = task_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int) -> bool:
    task = get_task(db, task_id)
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True
