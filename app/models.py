from sqlalchemy import Column, Integer, String, Date, Enum
from app.database import Base
import enum

class StatusEnum(str, enum.Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    due_date = Column(Date, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.new)
