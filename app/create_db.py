from app.database import Base, engine
from app.models import Task

print("Создание таблиц...")
Base.metadata.create_all(bind=engine)
print("Готово.")
