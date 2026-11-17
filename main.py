
from fastapi import FastAPI
import uvicorn

from routes.users import user_router
from routes.events import event_router

app = FastAPI(
    title="Event Planner API",
    description="API для планирования мероприятий",
    version="1.0.0"
)

# Подключаем маршруты пользователей
app.include_router(user_router, prefix="/user")

# Подключаем маршруты событий
app.include_router(event_router, prefix="/event")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        reload=True
    )
