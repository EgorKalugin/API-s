from typing import Any, Optional
from fastapi import Body, FastAPI

app = FastAPI()


# Обработчик GET-запросов на корневой URL
@app.get("/")
async def root_get_handler():
    # Возвращает JSON-объект с сообщением
    return {"message": "Hello, World!"}


# Обработчик POST-запросов на корневой URL
# Принимает JSON-данные в теле запроса
@app.post("/")
async def root_post_handler(body: Optional[Any] = Body(default=None)):
    # Выводит в консоль данные, полученные в теле запроса
    print(body)
    # Возвращает JSON-объект с сообщением
    if body is None:
        return {"message": "No data"}
    else:
        return {"message": f"Got {body}"}


# Запуск приложения с помощью Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app")
