from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from app.models import StatusEnum 

class TaskCreate(BaseModel):
    title: str = Field(..., example="Написать тестовое")
    description: Optional[str] = Field(None, example="Сделать REST API на FastAPI")
    due_date: Optional[date] = Field(None, example="2025-06-01")
    status: Optional[StatusEnum] = Field(StatusEnum.new, example="new")

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[StatusEnum] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: Optional[date]
    status: StatusEnum

    class Config:
        orm_mode = True
