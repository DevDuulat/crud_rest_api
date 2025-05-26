# crud_rest_api

# Task Manager API

Простое REST API для управления задачами, разработанное с использованием **FastAPI** и **SQLite**.

- Создание, чтение, обновление и удаление задач (CRUD).
- Поддержка полей: `title`, `description`, `due_date`, `status`.
- Фильтрация задач по статусу (`new`, `in_progress`, `done`) и по дате.
- Простая авторизация через токен (в заголовке запроса).
- Swagger-документация по адресу `/docs`.
- SQLite как база данных.

Поля задачи

| Поле        | Тип    | Обязательный | Описание                                    |
| ----------- | ------ | ------------ | ------------------------------------------- |
| title       | string | ✅           | Название задачи                             |
| description | string | ✅           | Описание задачи                             |
| due_date    | date   | ❌           | Дата дедлайна (в формате YYYY-MM-DD)        |
| status      | enum   | ❌           | Статус задачи: `new`, `in_progress`, `done` |

Авторизация

Все запросы требуют авторизации через заголовок:
Authorization: Bearer secret-token-123

## Локальный запуск

### Зависимости

Убедитесь, что у вас установлен **Python 3.8+** и **pip**.

Рекомендуется создать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Если у вас ещё нет `requirements.txt`, создайте его с таким содержимым:

```
fastapi
uvicorn
sqlalchemy
pydantic
```

### Запуск приложения

```bash
uvicorn main:app --reload
```

После запуска API будет доступен по адресу:

```
http://127.0.0.1:8000/
```

Swagger-документация:

```
http://127.0.0.1:8000/docs
```

### Инициализация базы данных

При первом запуске автоматически создаются таблицы. Также можно вручную:

```bash
python create_tables.py
```

## Примеры API-запросов

### Авторизация

Для доступа к API используется заголовок:

```

Authorization: Bearer secret-token-123

```

---

### Создать задачу (POST /tasks/)

```bash
curl -X POST http://127.0.0.1:8000/tasks/ \
  -H "Authorization: Bearer secret-token-123" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Написать тестовое",
    "description": "Сделать REST API на FastAPI",
    "due_date": "2025-06-01",
    "status": "new"
}'
```

---

### Получить список задач (GET /tasks/)

```bash
curl -H "Authorization: Bearer secret-token-123" \
  http://127.0.0.1:8000/tasks/
```

Фильтрация по статусу:

```bash
curl -H "Authorization: Bearer secret-token-123" \
  "http://127.0.0.1:8000/tasks/?status=new"
```

Фильтрация по дате:

```bash
curl -H "Authorization: Bearer secret-token-123" \
  "http://127.0.0.1:8000/tasks/?due_date=2025-06-01"
```

---

### Получить задачу по ID (GET /tasks/{id})

```bash
curl -H "Authorization: Bearer secret-token-123" \
  http://127.0.0.1:8000/tasks/1
```

---

### Обновить задачу (PUT /tasks/{id})

```bash
curl -X PUT http://127.0.0.1:8000/tasks/1 \
  -H "Authorization: Bearer secret-token-123" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Обновленная задача",
    "description": "Изменено",
    "due_date": "2025-06-02",
    "status": "in_progress"
}'
```

---

### Удалить задачу (DELETE /tasks/{id})

```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1 \
  -H "Authorization: Bearer secret-token-123"
```

## Рефлексия

### Что было самым сложным в задании?

Самым сложным оказалось организовать архитектуру проекта с учётом расширяемости, особенно при работе с FastAPI и SQLAlchemy. Также важно было правильно обрабатывать валидации и статус-коды, чтобы соответствовать REST-стандарту.

### Что получилось особенно хорошо?

Удалось быстро реализовать фильтрацию и CRUD через чистую архитектуру с разделением логики (schemas, models, crud). Swagger-документация автоматически работает из коробки это большой плюс FastAPI

### Что бы вы доработали при наличии времени?

- Добавил бы Docker для удобного запуска проекта.

### Сколько времени заняло выполнение?

Примерно 3–4 часа с нуля, включая настройку, написание кода и README.

### Чему вы научились при выполнении?

- Повторил принципы построения REST API на FastAPI.
- Улучшил навыки работы с зависимостями, валидацией, и обработкой ошибок.
- Потренировался писать документацию и оформлять проекты для передачи.
