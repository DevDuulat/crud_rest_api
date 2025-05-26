from fastapi import FastAPI, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from app.database import SessionLocal, engine
import app.models as models
import app.schemas as schemas
import app.crud as crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

API_TOKEN = "secret-token-123"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_token(authorization: Optional[str] = Header(None)):
    if authorization != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing token")

@app.get("/")
def root():
    return {"message": "Task Manager API is running"}

@app.post(
    "/tasks/",
    response_model=schemas.TaskOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_token)]
)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get(
    "/tasks/",
    response_model=List[schemas.TaskOut],
    dependencies=[Depends(verify_token)]
)
def list_tasks(
    status: Optional[schemas.StatusEnum] = None,
    due_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    return crud.get_tasks(db, status, due_date)

@app.get(
    "/tasks/{task_id}",
    response_model=schemas.TaskOut,
    dependencies=[Depends(verify_token)]
)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put(
    "/tasks/{task_id}",
    response_model=schemas.TaskOut,
    dependencies=[Depends(verify_token)]
)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(verify_token)]
)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
